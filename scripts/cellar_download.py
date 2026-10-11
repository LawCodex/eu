#!/usr/bin/env python3
"""Download the English text of every act listed in RAW/acts.json (and the Treaties)
from the Publications Office Cellar, using content negotiation on the CELEX URI.

Cache: RAW/html/<celex>.{html,pdf} + RAW/html/<celex>.json (status/url).  Re-runs skip
already-cached documents.  Concurrency is kept low (default 4) to be polite.
"""
import datetime
import json
import sys
import time
import random
import urllib.parse
from concurrent.futures import ThreadPoolExecutor, as_completed

import requests

from common import RAW, UA, CELLAR_CELEX
from treaties import TREATIES

HTML_ACCEPT = "application/xhtml+xml, text/html;q=0.9"
TODAY = datetime.date.today().isoformat()
CACHE = RAW / "html"


def fname(celex):
    return celex.replace("/", "_").replace("(", "_").replace(")", "_")


def get(celex, accept, retries=6):
    url = CELLAR_CELEX + urllib.parse.quote(celex, safe="")
    for i in range(retries):
        try:
            r = requests.get(url, headers={"User-Agent": UA, "Accept": accept,
                                           "Accept-Language": "eng"},
                             timeout=(30, 120), allow_redirects=True)
            if r.status_code in (200, 404, 406):
                return r
            if r.status_code == 300:
                return r
            err = f"HTTP {r.status_code}"
        except requests.RequestException as e:
            err = repr(e)
        wait = min(300, 5 * 2 ** i) + random.random() * 3
        print(f"  retry {celex} ({err}) in {wait:.0f}s", flush=True)
        time.sleep(wait)
    return None


def fetch_one(celex):
    base = CACHE / fname(celex)
    meta_p = base.with_suffix(".json")
    if meta_p.exists():
        return json.loads(meta_p.read_text())
    meta = {"celex": celex}
    r = get(celex, HTML_ACCEPT)
    if r is not None and r.status_code == 200 and "html" in r.headers.get("content-type", ""):
        base.with_suffix(".html").write_bytes(r.content)
        meta.update(status="ok", format="html", url=r.url)
    else:
        r2 = get(celex, "application/pdf")
        if r2 is not None and r2.status_code == 200 and "pdf" in r2.headers.get("content-type", ""):
            base.with_suffix(".pdf").write_bytes(r2.content)
            meta.update(status="ok", format="pdf", url=r2.url)
        else:
            meta.update(status="missing",
                        http=None if r is None else r.status_code,
                        ctype=None if r is None else r.headers.get("content-type"))
    meta_p.write_text(json.dumps(meta))
    return meta


def pick_version(act):
    """Latest consolidated version applicable today, else the original act."""
    cons = [c for c in act.get("consolidations", []) if c[1] <= TODAY]
    return cons[-1] if cons else None


def main(workers=4):
    CACHE.mkdir(parents=True, exist_ok=True)
    acts = json.loads((RAW / "acts.json").read_text())
    jobs = [t["celex"] for t in TREATIES]
    order = {"L": 0, "R": 1, "D": 2}
    for a in sorted(acts.values(), key=lambda a: (order.get(a["letter"], 9), a["celex"])):
        v = pick_version(a)
        jobs.append(v[0] if v else a["celex"])
    todo = [c for c in jobs if not (CACHE / (fname(c) + ".json")).exists()]
    print(f"{len(jobs)} documents, {len(todo)} to fetch", flush=True)
    done = 0
    with ThreadPoolExecutor(workers) as ex:
        futs = {ex.submit(fetch_one, c): c for c in todo}
        for f in as_completed(futs):
            done += 1
            m = f.result()
            if m.get("status") != "ok":
                print(f"  missing {futs[f]}: {m}", flush=True)
            if done % 200 == 0:
                print(f"{done}/{len(todo)}", flush=True)
    for t in TREATIES:
        if t.get("alt") and fetch_one(t["celex"]).get("status") != "ok":
            fetch_one(t["alt"])
    # second pass: consolidated version missing -> fall back to original act
    for a in acts.values():
        v = pick_version(a)
        if v:
            m = json.loads((CACHE / (fname(v[0]) + ".json")).read_text())
            if m.get("status") != "ok":
                fetch_one(a["celex"])
    print("done", flush=True)


if __name__ == "__main__":
    main(int(sys.argv[1]) if len(sys.argv) > 1 else 4)

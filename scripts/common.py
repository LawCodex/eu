"""Shared helpers for the LawCodex EU scripts."""
import os
import time
import random
import pathlib
import requests

ROOT = pathlib.Path(__file__).resolve().parent.parent          # repo root
RAW = pathlib.Path(os.environ.get("LAWCODEX_RAW",
                   ROOT.parent / "_raw" / "eu"))               # raw cache (not committed)
UA = "LawCodex/1.0 (+https://github.com/LawCodex)"
SPARQL = "https://publications.europa.eu/webapi/rdf/sparql"
CELLAR_CELEX = "http://publications.europa.eu/resource/celex/"

_session = None


def session():
    global _session
    if _session is None:
        s = requests.Session()
        s.headers["User-Agent"] = UA
        _session = s
    return _session


def sparql(query, retries=6):
    """Run a SPARQL query on the Publications Office endpoint, return list of dict rows."""
    for i in range(retries):
        try:
            r = session().post(SPARQL, data={"query": query},
                               headers={"Accept": "application/sparql-results+json"},
                               timeout=300)
            if r.status_code == 200:
                out = []
                for b in r.json()["results"]["bindings"]:
                    out.append({k: v["value"] for k, v in b.items()})
                return out
            err = f"HTTP {r.status_code}: {r.text[-300:]}"
        except Exception as e:  # noqa
            err = repr(e)
        wait = min(120, 5 * 2 ** i) + random.random()
        print(f"sparql retry {i+1}: {err}; sleeping {wait:.0f}s", flush=True)
        time.sleep(wait)
    raise RuntimeError("SPARQL query failed")

#!/usr/bin/env python3
"""Convert cached EUR-Lex/Cellar (X)HTML (or PDF) documents to LawCodex Markdown.

Handles the three HTML flavours served by Cellar:
  * OJ XHTML (2014+ acts):         classes oj-ti-art, oj-ti-section-1, oj-normal ...
  * OJ "formex" HTML (older acts):  classes ti-art, ti-section-1, normal ...
  * consolidated texts (CONSLEG):   classes title-article-norm, title-division-1, norm ...
  * legacy EUR-Lex HTML (no classes, <TXT_TE>): heading detection by text pattern.
"""
import datetime
import json
import re
import sys
import urllib.parse

import warnings
from bs4 import BeautifulSoup, NavigableString, Tag, XMLParsedAsHTMLWarning

warnings.filterwarnings("ignore", category=XMLParsedAsHTMLWarning)

from common import RAW, ROOT
from treaties import TREATIES

TODAY = datetime.date.today().isoformat()
CACHE = RAW / "html"
OUT = ROOT / "en"

TYPE_DIR = {"R": "regulations", "L": "directives", "D": "decisions"}
TYPE_NAME = {"R": "regulation", "L": "directive", "D": "decision"}

WS = re.compile(r"[ \t\r\n    ​]+")
MARKER = re.compile(r"[►▼]\s?(?:[A-Z]\d*|M\d+|C\d+|A\d+|B)\b\s?|◄")

SEC_KEYWORDS = [  # rank of structural divisions (smaller = higher)
    (re.compile(r"^(PART|Part)\b"), 1),
    (re.compile(r"^(TITLE|Title)\b"), 2),
    (re.compile(r"^(CHAPTER|Chapter)\b"), 3),
    (re.compile(r"^(SECTION|Section)\b"), 4),
    (re.compile(r"^(SUBSECTION|Subsection|Sub-section|SUB-SECTION)\b"), 5),
]
ANNEX_RE = re.compile(r"^(ANNEX|Annex|APPENDIX|Appendix)\b")
ART_RE = re.compile(r"^(Article|ARTICLE)\s+\d+[a-z]*(\s*\(?[a-z]+\)?)?\.?$|^(Sole Article|Single Article)$")
LEGACY_SEC_RE = re.compile(r"^(PART|TITLE|CHAPTER|SECTION|Part|Title|Chapter|Section)\s+([IVXLC]+|\d+|ONE|TWO|THREE|FOUR|FIVE|SIX|SEVEN|EIGHT|NINE|TEN)\b")

HEAD_CLASSES = {"hd-date", "hd-lg", "hd-ti", "hd-oj", "separator", "doc-end", "modref",
                "arrow", "separator-short", "disclaimer", "reference", "hd-modifiers",
                "title-doc-oj-reference", "title-fam-member"}
SKIP_IDS = {"banner"}


def norm(s):
    s = WS.sub(" ", s)
    s = MARKER.sub("", s)
    return s.strip()


def clean_classes(el):
    return [c[3:] if c.startswith("oj-") else c for c in (el.get("class") or [])]


class Converter:
    def __init__(self, base_url):
        self.base_url = base_url
        self.events = []        # (kind, payload)
        self.prefix = ""        # pending list label to prepend to next paragraph
        self.pending_sec = None
        self.pending_art = None

    # ---------- inline text ----------
    def inline(self, el):
        parts = []
        for node in el.descendants:
            if isinstance(node, NavigableString):
                if node.parent.name in ("script", "style"):
                    continue
                parts.append(str(node))
            elif isinstance(node, Tag):
                if node.name == "br":
                    parts.append(" ")
                elif node.name == "img":
                    src = node.get("src")
                    if src and src.startswith("data:"):
                        parts.append(" [image] ")
                    elif src:
                        url = urllib.parse.urljoin(self.base_url, src)
                        alt = norm(node.get("alt", "")) or "image"
                        parts.append(f" ![{alt}]({url}) ")
        return norm("".join(parts))

    # ---------- emit ----------
    def para(self, text):
        if not text:
            return
        self.flush_heading()
        if self.prefix:
            text = f"{self.prefix} {text}"
            self.prefix = ""
        self.events.append(("p", text))

    def flush_prefix(self):
        if self.prefix:
            p, self.prefix = self.prefix, ""
            self.flush_heading()
            self.events.append(("p", p))

    def flush_heading(self):
        if self.pending_sec:
            rank, parts = self.pending_sec
            self.pending_sec = None
            self.events.append(("sec", rank, " — ".join(parts)))
        if self.pending_art:
            parts = self.pending_art
            self.pending_art = None
            self.events.append(("art", " — ".join(parts)))

    def section(self, text, sub=False):
        if not text:
            return
        if sub and self.pending_sec:
            self.pending_sec[1].append(text)
            return
        self.flush_prefix()
        self.flush_heading()
        rank = 3
        if ANNEX_RE.match(text):
            rank = 0
        else:
            for rx, r in SEC_KEYWORDS:
                if rx.match(text):
                    rank = r
                    break
            else:
                if sub:  # orphan subtitle -> paragraph
                    self.events.append(("b", text))
                    return
        self.pending_sec = (rank, [text])

    def article(self, text):
        self.flush_prefix()
        self.flush_heading()
        self.pending_art = [text]

    def article_sub(self, text):
        if self.pending_art:
            self.pending_art.append(text)
        elif text:
            self.para(text)

    # ---------- tables ----------
    def table(self, t):
        rows = [r for r in t.find_all("tr") if r.find_parent("table") is t]
        if not rows:
            return
        cls = clean_classes(t)
        if t.find(class_=re.compile(r"(^|-)hd-(date|oj|lg)$")):
            return  # OJ page header
        # layout table used for numbered lists: 2 cells, short label in first
        if "table" not in cls:
            is_list = True
            for r in rows:
                cells = [c for c in r.find_all(["td", "th"], recursive=False)]
                if len(cells) != 2 or len(self.inline(cells[0])) > 14:
                    is_list = False
                    break
            if is_list:
                for r in rows:
                    c0, c1 = r.find_all(["td", "th"], recursive=False)
                    lab = self.inline(c0)
                    self.flush_prefix()
                    self.prefix = lab
                    self.walk(c1)
                    self.flush_prefix()
                return
            # single-cell layout wrappers
            if all(len(r.find_all(["td", "th"], recursive=False)) == 1 for r in rows):
                for r in rows:
                    self.walk(r.find(["td", "th"], recursive=False))
                return
        self.flush_prefix()
        self.flush_heading()
        nested = t.find("table") is not None
        spans = any(c.get("colspan", "1") not in ("1", "") or c.get("rowspan", "1") not in ("1", "")
                    for c in t.find_all(["td", "th"]))
        grid = []
        for r in rows:
            grid.append([self.inline(c).replace("|", "\\|") for c in r.find_all(["td", "th"], recursive=False)])
        width = max((len(g) for g in grid), default=0)
        if not nested and not spans and width >= 1 and len(grid) >= 1:
            lines = []
            for i, g in enumerate(grid):
                g = g + [""] * (width - len(g))
                lines.append("| " + " | ".join(g) + " |")
                if i == 0:
                    lines.append("|" + " --- |" * width)
            self.events.append(("raw", "\n".join(lines)))
        else:
            self.events.append(("raw", self.html_table(t)))

    def html_table(self, t):
        def rec(el):
            out = []
            for node in el.children:
                if isinstance(node, NavigableString):
                    s = WS.sub(" ", str(node))
                    if s.strip():
                        out.append(s.replace("<", "&lt;").replace(">", "&gt;"))
                elif isinstance(node, Tag):
                    if node.name in ("table", "tr", "td", "th", "thead", "tbody", "tfoot"):
                        attrs = ""
                        for a in ("colspan", "rowspan"):
                            if node.get(a) and node.get(a) != "1":
                                attrs += f' {a}="{node.get(a)}"'
                        inner = rec(node)
                        out.append(f"<{node.name}{attrs}>{inner}</{node.name}>")
                        if node.name in ("tr", "table", "thead", "tbody"):
                            out.append("\n")
                    elif node.name == "br":
                        out.append("<br>")
                    elif node.name == "img":
                        src = node.get("src", "")
                        if src.startswith("data:"):
                            out.append("[image]")
                            continue
                        src = urllib.parse.urljoin(self.base_url, src)
                        out.append(f'<img src="{src}" alt="{node.get("alt", "")}">')
                    elif node.name in ("p", "div") and out:
                        out.append(" " + rec(node).strip() + " ")
                    elif node.name in ("colgroup", "col"):
                        continue
                    else:
                        out.append(rec(node))
            return MARKER.sub("", "".join(out))
        return "<table>\n" + rec(t).strip() + "\n</table>"

    # ---------- walk ----------
    def walk(self, el):
        for node in list(el.children):
            if isinstance(node, NavigableString):
                s = norm(str(node))
                if s and node.parent.name not in ("script", "style", "table", "tr", "tbody"):
                    self.para(s)
                continue
            if not isinstance(node, Tag):
                continue
            self.block(node)

    def block(self, el):
        name = el.name
        if name in ("script", "style", "head", "hr", "col", "colgroup", "meta", "link", "title"):
            return
        if el.get("id") in SKIP_IDS:
            return
        cls = clean_classes(el)
        if set(cls) & HEAD_CLASSES:
            return
        if name == "table":
            return self.table(el)
        text_cls = set(cls)
        if text_cls & {"ti-art", "title-article-norm"}:
            return self.article(self.inline(el))
        if text_cls & {"sti-art", "stitle-article-norm"}:
            return self.article_sub(self.inline(el))
        if text_cls & {"ti-section-1", "title-division-1", "title-annex-1"}:
            return self.section(self.inline(el))
        if text_cls & {"ti-section-2", "title-division-2", "title-annex-2"}:
            return self.section(self.inline(el), sub=True)
        if text_cls & {"doc-ti", "title-doc-first", "title-doc-last"}:
            t = self.inline(el)
            if ANNEX_RE.match(t) or t.startswith("APPENDIX"):
                return self.section(t)
            if self.pending_sec and self.pending_sec[0] == 0:
                return self.section(t, sub=True)
            self.flush_prefix()
            self.flush_heading()
            return self.events.append(("b", t)) if t else None
        if text_cls & {"ti-grseq-1", "ti-tbl", "title-gr-seq-level-1", "title-gr-seq-level-2",
                       "title-gr-seq-level-3", "title-table"}:
            t = self.inline(el)
            if t:
                self.flush_prefix()
                self.flush_heading()
                self.events.append(("b", t))
            return
        if "grid-container" in cls:
            lab = None
            for c in el.find_all("div", recursive=False):
                cc = clean_classes(c)
                if "grid-list-column-1" in cc:
                    lab = self.inline(c)
                elif "grid-list-column-2" in cc:
                    self.flush_prefix()
                    self.prefix = lab or ""
                    self.walk(c)
                    self.flush_prefix()
                else:
                    self.block(c)
            return
        if name == "span" and "no-parag" in cls:
            self.flush_prefix()
            self.prefix = self.inline(el)
            return
        # a container with block children -> recurse; else it's a paragraph
        has_block = el.find(["p", "div", "table", "ul", "ol", "li", "h1", "h2", "h3", "h4",
                             "h5", "h6", "txt_te", "dl", "blockquote"]) is not None
        if name in ("ul", "ol"):
            for li in el.find_all("li", recursive=False):
                self.flush_prefix()
                self.prefix = "-"
                self.walk(li)
                self.flush_prefix()
            return
        if has_block:
            return self.walk(el)
        if name in ("span", "a", "b", "i", "em", "strong", "sup", "sub", "font", "u") and \
                el.parent is not None and el.parent.name in ("div",) and self.prefix:
            # inline content directly following a label inside a div
            return self.para(self.inline(el))
        t = self.inline(el)
        if not t:
            return
        if self.legacy:
            if ART_RE.match(t):
                return self.article(t)
            if LEGACY_SEC_RE.match(t) and len(t) < 200:
                return self.section(t)
            if ANNEX_RE.match(t) and len(t) < 120:
                return self.section(t)
        self.para(t)

    legacy = False

    def run(self, root, legacy=False):
        self.legacy = legacy
        self.walk(root)
        self.flush_prefix()
        self.flush_heading()
        return self.events


def render(events):
    ranks = sorted({e[1] for e in events if e[0] == "sec" and e[1] > 0})
    level_of = {r: min(2 + i, 6) for i, r in enumerate(ranks)}
    art_level = min(2 + len(ranks), 6)
    out = []
    in_annex = False
    for e in events:
        k = e[0]
        if k == "sec":
            rank, text = e[1], e[2]
            if rank == 0:
                in_annex = True
                out.append(f"## {text}")
            else:
                lvl = level_of[rank] + (1 if in_annex and level_of[rank] < 6 else 0)
                out.append("#" * lvl + " " + text)
        elif k == "art":
            out.append("#" * art_level + " " + e[1])
        elif k == "b":
            out.append(f"**{escape_md(e[1])}**")
        elif k == "p":
            out.append(escape_md(e[1]))
        elif k == "raw":
            out.append(e[1])
    return "\n\n".join(out)


def escape_md(s):
    # avoid accidental headings / list markers / html at line start
    if s.startswith("#"):
        s = "\\" + s
    if re.match(r"^\d+\.\s", s):
        s = re.sub(r"^(\d+)\.", r"\1\\.", s)
    s = s.replace("<", "&lt;") if "![" not in s else s
    return s


def html_to_md(path, base_url):
    raw = path.read_bytes()
    soup = BeautifulSoup(raw, "lxml")
    body = soup.body or soup
    legacy = False
    txt = soup.find("txt_te")
    if txt is not None:
        body, legacy = txt, True
    elif soup.find(id="TexteOnly") is not None:
        body, legacy = soup.find(id="TexteOnly"), True
    elif not soup.find(class_=re.compile(r"^(oj-)?(normal|norm|ti-art|title-article-norm)$")):
        legacy = True
    conv = Converter(base_url)
    events = conv.run(body, legacy=legacy)
    return render(events)


PDF_BREAK = re.compile(r"^(Article \d+|ARTICLE \d+|\(\w{1,5}\)\s|\d{1,3}\.\s|[—–-]\s|CHAPTER|TITLE|SECTION|PART|ANNEX|Whereas|Having regard|HAS ADOPTED|HAVE ADOPTED|Done at|For the )")


def pdf_to_md(path):
    import logging
    logging.getLogger("pypdf").setLevel(logging.ERROR)
    from pypdf import PdfReader
    reader = PdfReader(str(path))
    paras, cur = [], []
    for page in reader.pages:
        t = page.extract_text() or ""
        for line in t.splitlines():
            line = norm(line)
            if not line:
                continue
            # drop running headers of consolidated PDFs ("1982R1985 — EN — 01.03.1986 — 001.001 — 2")
            if re.match(r"^\d{4}[A-Z]\d{4} — [A-Z]{2} — [\d.]+ — [\d.]+ — \d+", line):
                line = re.sub(r"^\d{4}[A-Z]\d{4} — [A-Z]{2} — [\d.]+ — [\d.]+ — \d+\s*", "", line)
                if not line:
                    continue
            if cur and (PDF_BREAK.match(line) or re.search(r"[.;:]$", cur[-1]) or ART_RE.match(cur[-1])):
                paras.append(cur)
                cur = []
            cur.append(line)
    if cur:
        paras.append(cur)
    conv = Converter("")
    conv.legacy = True
    for p in paras:
        text = ""
        for l in p:
            if text.endswith("-") and l[:1].islower():
                text = text[:-1] + l
            else:
                text = (text + " " + l).strip()
        if ART_RE.match(text):
            conv.article(text)
        elif LEGACY_SEC_RE.match(text) and len(text) < 200:
            conv.section(text)
        elif ANNEX_RE.match(text) and len(text) < 120:
            conv.section(text)
        else:
            conv.para(text)
    conv.flush_prefix()
    conv.flush_heading()
    return render(conv.events)


# ---------------- metadata / filenames ----------------

def slugify(s, maxlen=80):
    import unicodedata
    s = unicodedata.normalize("NFKD", s).encode("ascii", "ignore").decode()
    s = re.sub(r"[^a-zA-Z0-9]+", "-", s.lower()).strip("-")
    if len(s) > maxlen:
        s = s[:maxlen].rsplit("-", 1)[0]
    return s


SHORT_RE = re.compile(r"\(([^()]*?(?:Regulation|Directive|Act|Code|Decision|Statute|Rules|Framework)[^()]*)\)")


def short_slug(title):
    t = re.sub(r"\s*\(?Text with EEA relevance\.?\s*\)?\s*$", "", title, flags=re.I).strip()
    t = re.sub(r"\(?\s*Text with EEA relevance\.?\s*\)?", "", t, flags=re.I)
    m = None
    for m_ in SHORT_RE.finditer(t):
        m = m_
    if m and m.end() >= len(t) - 2 and len(m.group(1)) < 80 and not re.search(r"\d{4}/\d+|No \d+", m.group(1)) \
            and "codified" not in m.group(1).lower() and "recast" not in m.group(1).lower():
        return slugify(m.group(1))
    # strip the leading "Regulation (EU) 2016/679 of the ... of 27 April 2016"
    m2 = re.search(r"\b\d{1,2}\s+(January|February|March|April|May|June|July|August|September|"
                   r"October|November|December)\s+\d{4}\s*", t)
    rest = t[m2.end():] if m2 and m2.start() < 250 else t
    rest = re.sub(r"^[,\s]*", "", rest)
    return slugify(rest, 70) or slugify(t, 70)


def yaml_str(s):
    return '"' + s.replace("\\", "\\\\").replace('"', '\\"') + '"'


def front_matter(fm):
    lines = ["---"]
    for k, v in fm.items():
        if v is None or v == "":
            continue
        if isinstance(v, str) and not re.match(r"^\d{4}-\d{2}-\d{2}$", v) and k not in ("type", "jurisdiction", "language", "status", "subtype"):
            v = yaml_str(v)
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def fname(celex):
    return celex.replace("/", "_").replace("(", "_").replace(")", "_")


def load_meta(celex):
    p = CACHE / (fname(celex) + ".json")
    if not p.exists():
        return None
    m = json.loads(p.read_text())
    return m if m.get("status") == "ok" else None


def body_for(celex, meta):
    base = CACHE / fname(celex)
    if meta["format"] == "html":
        return html_to_md(base.with_suffix(".html"), meta["url"])
    return pdf_to_md(base.with_suffix(".pdf"))


def eurlex(celex):
    return "https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:" + urllib.parse.quote(celex, safe=":")


def clean_title(t):
    t = norm(t)
    t = re.sub(r"#.*$", "", t) if "#" in t else t
    return t


def write(path, fm, title, body):
    path.parent.mkdir(parents=True, exist_ok=True)
    text = front_matter(fm) + "\n\n# " + title + "\n\n" + body.strip() + "\n"
    path.write_text(text, encoding="utf-8")


def convert_treaties(stats):
    for t in TREATIES:
        celex = t["celex"]
        meta = load_meta(celex)
        if not meta and t.get("alt"):
            celex = t["alt"]
            meta = load_meta(celex)
        if not meta:
            stats["missing"].append(t["celex"])
            continue
        body = body_for(celex, meta)
        title = t.get("title")
        slug = t["slug"]
        if not title:
            heads = [re.sub(r"^(\*\*|#+ )|\*\*$", "", l).replace("\\", "").strip()
                     for l in body.splitlines() if l.startswith(("**", "#"))][:2]
            title = heads[0] if heads else t["celex"]
            if re.match(r"^(PROTOCOL|ANNEX)", title) and len(heads) > 1:
                title = f"{title} {heads[1]}"
                slug = f"{slug}-{slugify(heads[1], 70)}"
            else:
                slug = f"{slug}-{slugify(re.sub(r'^[0-9.]+ *(Declaration )?', '', title, flags=re.I), 70)}"
        d = OUT / "treaties" / t.get("dir", "")
        fm = {"title": title, "identifier": celex, "type": "treaty", "jurisdiction": "eu",
              "language": "en", "date": "2016-06-07" if celex.startswith("12016") else None,
              "status": "in_force", "source": eurlex(celex), "retrieved": TODAY}
        write(d / (slug.rstrip("-") + ".md"), fm, title, body)
        stats["treaties"] += 1


SUBTYPE = {"REG_IMPL": "implementing", "REG_DEL": "delegated", "DIR_IMPL": "implementing",
           "DIR_DEL": "delegated", "DEC_IMPL": "implementing", "DEC_DEL": "delegated",
           "DEC_ENTSCHEID": "addressed", "DEC_FRAMW": "framework", "REG_FINANC": "financial"}


def main(letters):
    acts = json.loads((RAW / "acts.json").read_text())
    stats = {"treaties": 0, "missing": [], "consolidated": 0, "original": 0}
    import shutil
    for l in letters:  # rebuild each requested category from scratch (drops stale files)
        shutil.rmtree(OUT / ("treaties" if l == "T" else TYPE_DIR[l]), ignore_errors=True)
    if "T" in letters:
        convert_treaties(stats)
    counts = {}
    per_year = {}
    for c, a in acts.items():
        per_year[(a["letter"], c[1:5])] = per_year.get((a["letter"], c[1:5]), 0) + 1
    for c, a in sorted(acts.items()):
        if a["letter"] not in letters:
            continue
        cons = [x for x in a["consolidations"] if x[1] <= TODAY]
        used, cdate = a["celex"], None
        meta = None
        if cons:
            meta = load_meta(cons[-1][0])
            if meta:
                used, cdate = cons[-1]
        if meta is None:
            meta = load_meta(a["celex"])
        if meta is None:
            stats["missing"].append(c)
            continue
        try:
            body = body_for(used, meta)
        except Exception as e:  # noqa
            print("convert error", c, e, file=sys.stderr)
            stats["missing"].append(c)
            continue
        if len(body.strip()) < 20:
            stats["missing"].append(c)
            continue
        title = clean_title(a["title"]) or c
        year = c[1:5]
        slug = short_slug(title)
        fn = f"{c.lower()}-{slug}".rstrip("-")[:100].rstrip("-") + ".md"
        fm = {"title": title, "identifier": c, "eli": a.get("eli"),
              "type": TYPE_NAME[a["letter"]], "subtype": SUBTYPE.get(a["rtype"]),
              "jurisdiction": "eu", "language": "en", "date": a["date"] or None,
              "entry_into_force": a.get("eif") or None,
              "last_amended": cdate, "consolidated_version": used if cdate else None,
              "status": "in_force", "source": eurlex(used), "retrieved": TODAY}
        d = OUT / TYPE_DIR[a["letter"]] / year
        if per_year[(a["letter"], year)] > 900:
            # keep directories under GitHub's 1,000-entry listing limit
            num = int(re.sub(r"\D.*$", "", c[6:]) or 0)
            lo = num // 500 * 500
            d = d / f"{lo:04d}-{lo + 499:04d}"
        write(d / fn, fm, title, body)
        stats["consolidated" if cdate else "original"] += 1
        counts[a["letter"]] = counts.get(a["letter"], 0) + 1
    stats["counts"] = counts
    (RAW / f"stats-{''.join(letters)}.json").write_text(json.dumps(stats, indent=1))
    print(json.dumps({k: (v if k != "missing" else len(v)) for k, v in stats.items()}))


if __name__ == "__main__":
    main(sys.argv[1:] or ["T", "R", "L", "D"])

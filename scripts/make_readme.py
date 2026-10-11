#!/usr/bin/env python3
"""Regenerate README.md with current counts."""
import collections
import datetime
import json
import re

from common import RAW, ROOT

EN = ROOT / "en"


def count(sub):
    files = list((EN / sub).rglob("*.md")) if (EN / sub).exists() else []
    cons = 0
    sub_c = collections.Counter()
    for f in files:
        head = f.read_text(encoding="utf-8")[:3000]
        if "\nconsolidated_version:" in head:
            cons += 1
        m = re.search(r"\nsubtype: (\w+)", head)
        sub_c[m.group(1) if m else "-"] += 1
    return len(files), cons, sub_c


def main():
    today = datetime.date.today().isoformat()
    acts = json.loads((RAW / "acts.json").read_text())
    listed = collections.Counter(a["letter"] for a in acts.values())
    t_n = len(list((EN / "treaties").rglob("*.md")))
    rows = []
    for letter, sub, label in (("R", "regulations", "Regulations"), ("L", "directives", "Directives"),
                               ("D", "decisions", "Decisions")):
        n, cons, sc = count(sub)
        detail = ", ".join(f"{k}: {v}" for k, v in sorted(sc.items()) if k != "-")
        rows.append(f"| {label} | `en/{sub}/` | {listed.get(letter, 0)} | {n} | {cons} | {detail or '-'} |")
    total = t_n + sum(int(r.split("|")[4]) for r in rows)
    text = f"""# European Union legislation — LawCodex

The law of the **European Union** as plain Markdown: the consolidated Treaties and every
regulation, directive and decision that EUR-Lex marks as **in force**, in English, using the
latest consolidated version where the Publications Office publishes one.

Part of [LawCodex](https://github.com/LawCodex) — one repository per jurisdiction.

Retrieved: **{today}** — {total} documents.

## Contents

| Category | Directory | In force (listed) | Files | Consolidated text | Sub-types |
| --- | --- | ---: | ---: | ---: | --- |
| Treaties (TEU, TFEU, Charter, Euratom, protocols, annexes, declarations) | `en/treaties/` | — | {t_n} | (2016 consolidated versions) | — |
{chr(10).join(rows)}

"In force (listed)" is the number of acts flagged in force in Cellar metadata; the difference with
"Files" are acts for which no English text (HTML/XHTML or PDF) is available in Cellar — mostly
pre-1973 acts never published in an English special edition, and some acts published only as
scanned print. "Consolidated text" counts files built from a consolidated version (CELEX sector 0)
rather than the original Official Journal text. Sub-types: implementing / delegated acts,
"addressed" = decisions with addressees (*Entscheidung*), "framework" = former third-pillar framework
decisions.

## Structure

```
en/
  treaties/                      TEU, TFEU, Charter of Fundamental Rights, Euratom Treaty
    protocols/                   the 37 protocols annexed to the TEU/TFEU
    declarations/                the 65 declarations annexed to the Final Act of the Lisbon IGC
    tfeu-annexes/  euratom-annexes/
  regulations/<year>/            one file per regulation, named <celex>-<slug>.md
  directives/<year>/
  decisions/<year>/
```

Years with more than 900 acts of one type are split into CELEX number ranges
(`<year>/0000-0499/`, `<year>/0500-0999/`, ...) so that no directory exceeds GitHub's 1,000-entry
listing limit. File names start with the CELEX number of the act (e.g.
`regulations/2016/32016r0679-general-data-protection-regulation.md`).

Each file has YAML front matter: `title`, `identifier` (CELEX of the base act), `eli`, `type`
(`treaty` / `regulation` / `directive` / `decision`), `subtype`, `date` (date of the act),
`entry_into_force`, `last_amended` + `consolidated_version` (date and CELEX of the consolidated
version used, when applicable), `status`, `source` (EUR-Lex link to the exact text used) and
`retrieved`. The body keeps the act's structure: parts / titles / chapters / sections as headings,
articles as the deepest heading level; numbered points as paragraphs; tables as Markdown tables
(simple) or HTML (with merged cells).

## What is NOT covered

- Acts no longer in force (repealed / expired), and international agreements, case law,
  preparatory acts, national transposition measures.
- Other languages (all 24 official languages exist in EUR-Lex; only English is included).
- Embedded images that Cellar inlines as `data:` URIs (mostly formulas and diagrams in annexes)
  are replaced by `[image]`; other images are linked to their Cellar URL.
- Consolidated versions are documentation tools: only the texts published in the Official Journal
  are authentic. Consolidations dated in the future (amendments not yet applicable) are not used;
  the latest consolidation applicable on the retrieval date is.
- Acts in force without any English manifestation in Cellar (see counts above).
- About 50 texts exist in Cellar only as PDF; they were converted by text extraction (pypdf), so
  their layout is flatter and some words may be run together.

## Sources

- Publications Office of the EU — Cellar SPARQL endpoint
  <https://publications.europa.eu/webapi/rdf/sparql> (list of acts in force, metadata,
  consolidated versions), and Cellar content negotiation on
  `http://publications.europa.eu/resource/celex/<CELEX>` (XHTML/HTML, PDF as fallback).
- Human-readable copies: [EUR-Lex](https://eur-lex.europa.eu/) (links in each file's `source`).

## Licence

EU legislation published on EUR-Lex may be reused under the Commission's reuse policy
(Decision 2011/833/EU; content © European Union, https://eur-lex.europa.eu/content/legal-notice/legal-notice.html):
reuse is authorised provided the source is acknowledged. Only the Official Journal of the
European Union (electronic edition) is authentic. The conversion scripts in `scripts/` are offered
under the same terms as the rest of LawCodex.

## Regenerating

```sh
python -m venv .venv && .venv/bin/pip install -r scripts/requirements.txt
cd scripts
python list_acts.py R L D     # SPARQL: acts in force + consolidated versions -> ../_raw/eu/acts.json
python cellar_download.py 4            # download (X)HTML/PDF to ../_raw/eu/html (cached, 4 workers)
python convert.py T R L D     # write en/
python make_readme.py
```

Raw downloads go to `../_raw/eu/` (override with `LAWCODEX_RAW`) and are not committed.
"""
    (ROOT / "README.md").write_text(text, encoding="utf-8")
    print("README written", total)


if __name__ == "__main__":
    main()

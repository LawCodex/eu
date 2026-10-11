#!/usr/bin/env python3
"""List EU regulations, directives and decisions currently in force (sector 3 CELEX)
plus their consolidated versions, using the Publications Office SPARQL endpoint.

Writes RAW/acts.json : {celex: {...metadata..., "consolidations": [[celex, date], ...]}}
"""
import datetime
import json
import sys
from common import RAW, sparql

XSD = "http://www.w3.org/2001/XMLSchema#"
PAGE = 5000


def base_acts(letter, year):
    rows, off = [], 0
    while True:
        q = f"""
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?celex (SAMPLE(?rt) AS ?rtype) (SAMPLE(?d) AS ?date) (SAMPLE(?t) AS ?title)
       (MIN(?eif) AS ?eif) (SAMPLE(?el) AS ?eli) WHERE {{
  ?w cdm:resource_legal_id_sector "3"^^<{XSD}string> ;
     cdm:resource_legal_in-force "true"^^<{XSD}boolean> ;
     cdm:resource_legal_type "{letter}"^^<{XSD}string> ;
     cdm:resource_legal_id_celex ?celex ;
     cdm:work_has_resource-type ?rt .
  FILTER(STRSTARTS(STR(?celex), "3{year}{letter}"))
  OPTIONAL {{ ?w cdm:work_date_document ?d }}
  OPTIONAL {{ ?w cdm:resource_legal_date_entry-into-force ?eif }}
  OPTIONAL {{ ?w cdm:resource_legal_eli ?el }}
  OPTIONAL {{ ?e cdm:expression_belongs_to_work ?w ;
               cdm:expression_uses_language <http://publications.europa.eu/resource/authority/language/ENG> ;
               cdm:expression_title ?t }}
}} GROUP BY ?celex ORDER BY ?celex LIMIT {PAGE} OFFSET {off}"""
        page = sparql(q)
        rows += page
        if len(page) < PAGE:
            return rows
        off += PAGE


def consolidations(letter, year):
    rows, off = [], 0
    while True:
        q = f"""
PREFIX cdm: <http://publications.europa.eu/ontology/cdm#>
SELECT ?celex ?cc ?cd WHERE {{
  ?w cdm:resource_legal_id_sector "3"^^<{XSD}string> ;
     cdm:resource_legal_in-force "true"^^<{XSD}boolean> ;
     cdm:resource_legal_type "{letter}"^^<{XSD}string> ;
     cdm:resource_legal_id_celex ?celex .
  FILTER(STRSTARTS(STR(?celex), "3{year}{letter}"))
  ?c cdm:act_consolidated_based_on_resource_legal ?w ;
     cdm:resource_legal_id_celex ?cc ;
     cdm:act_consolidated_date ?cd .
}} ORDER BY ?celex ?cc LIMIT {PAGE} OFFSET {off}"""
        page = sparql(q)
        rows += page
        if len(page) < PAGE:
            return rows
        off += PAGE


def main(letters):
    RAW.mkdir(parents=True, exist_ok=True)
    acts = {}
    years = range(1952, datetime.date.today().year + 1)
    for letter in letters:
        for year in years:
            for r in base_acts(letter, year):
                c = r["celex"]
                # skip corrigenda and other non-act CELEX forms
                if "(" in c or not c[1:5].isdigit():
                    continue
                acts[c] = {
                    "celex": c, "letter": letter,
                    "rtype": r.get("rtype", "").rsplit("/", 1)[-1],
                    "date": r.get("date", "")[:10],
                    "eif": r.get("eif", "")[:10],
                    "eli": r.get("eli", ""),
                    "title": r.get("title", ""),
                    "consolidations": [],
                }
            for r in consolidations(letter, year):
                a = acts.get(r["celex"])
                if a is not None:
                    a["consolidations"].append([r["cc"], r["cd"][:10]])
            print(f"  {letter} {year}: total {len(acts)}", flush=True)
    for a in acts.values():
        a["consolidations"] = sorted(set(map(tuple, a["consolidations"])), key=lambda x: x[1])
    out = RAW / "acts.json"
    out.write_text(json.dumps(acts, indent=0, ensure_ascii=False))
    print(f"wrote {len(acts)} acts to {out}")


if __name__ == "__main__":
    main(sys.argv[1:] or ["R", "L", "D"])

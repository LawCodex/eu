"""The consolidated Treaties (OJ C 202, 7.6.2016 and OJ C 203 for Euratom), by CELEX."""

TREATIES = [
    {"celex": "12016M/TXT", "slug": "teu-treaty-on-european-union",
     "title": "Consolidated version of the Treaty on European Union"},
    {"celex": "12016E/TXT", "slug": "tfeu-treaty-on-the-functioning-of-the-european-union",
     "title": "Consolidated version of the Treaty on the Functioning of the European Union"},
    {"celex": "12016P/TXT", "slug": "charter-of-fundamental-rights-of-the-european-union",
     "title": "Charter of Fundamental Rights of the European Union"},
    {"celex": "12016A/TXT", "slug": "euratom-treaty-establishing-the-european-atomic-energy-community",
     "title": "Consolidated version of the Treaty establishing the European Atomic Energy Community"},
]
# Annexes to the TFEU / Euratom
for i in (1, 2):
    TREATIES.append({"celex": f"12016EN{i:02d}", "dir": "tfeu-annexes", "slug": f"annex-{i}"})
for i in (1, 2, 3, 4):
    TREATIES.append({"celex": f"12016AN{i:02d}", "dir": "euratom-annexes", "slug": f"annex-{i}"})
# Protocols annexed to the TEU/TFEU (same 37 protocols annexed to both; TFEU CELEX used)
for i in range(1, 38):
    TREATIES.append({"celex": f"12016E/PRO/{i:02d}", "dir": "protocols", "slug": f"protocol-{i:02d}"})
# Declarations annexed to the Final Act of the Lisbon IGC
for i in range(1, 66):
    # a few 2016 declarations have no English text in Cellar: fall back to the 2012 edition
    TREATIES.append({"celex": f"12016L/AFI/DCL/{i:02d}", "alt": f"12012L/AFI/DCL/{i:02d}",
                     "dir": "declarations", "slug": f"declaration-{i:02d}"})

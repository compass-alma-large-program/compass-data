"""
Export Serp-11 setting 2 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X117bb05_X8747", "uid___A002_X117bb05_X8142"],
    field="Ser_emb_11_W",
    basename="serp11-set2",
)

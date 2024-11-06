"""
Export Serp-11 setting 1 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X1175218_X1092a",
        "uid___A002_X117a165_X3995",
        "uid___A002_X117a165_X489f",
    ],
    field="Ser_emb_11_W",
    basename="serp11-set1",
)

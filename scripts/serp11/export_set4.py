"""
Export Serp-11 setting 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X117a165_X508e",
        "uid___A002_X117a165_X4143",
        "uid___A002_X1175218_Xa35c",
    ],
    field="Ser_emb_11_W",
    basename="serp11-set4",
)

"""
Export Serp-11 setting 8 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1175218_X9c02", "uid___A002_X1175218_X945d"],
    field="Ser_emb_11_W",
    basename="serp11-set8",
)

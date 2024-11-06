"""
Export Serp-11 setting 6 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X4443", "uid___A002_X1175218_X3e66"],
    field="Ser_emb_11_W",
    basename="serp11-set6",
)

"""
Export Serp-11 setting 9 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X3763", "uid___A002_X1173aab_X9768"],
    field="Ser_emb_11_W",
    basename="serp11-set9",
)

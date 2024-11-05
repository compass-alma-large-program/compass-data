"""
Export Serp-11 setting 3 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X117d38c_X17cb",
        "uid___A002_X117d38c_X87e1",
        "uid___A002_X117d38c_Xec1e",
    ],
    field="Ser_emb_11_W",
    basename="serp11-set3",
)

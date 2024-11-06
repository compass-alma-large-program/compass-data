"""
Export Serp-11 setting 5 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X117d38c_X203f9",
        "uid___A002_X11adad7_X1c75d",
    ],
    field="Ser_emb_11_W",
    basename="serp11-set5",
)

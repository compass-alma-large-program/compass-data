"""
Export Serp-11 setting 7 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1173aab_Xa09c", "uid___A002_X1173aab_Xa728"],
    field="Ser_emb_11_W",
    basename="serp11-set7",
)

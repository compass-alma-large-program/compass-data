"""
Export Serp-1a setting 7 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1173aab_Xa09c", "uid___A002_X1173aab_Xa728"],
    field="Serp_SMM1-a",
    basename="serp1a-set7",
)

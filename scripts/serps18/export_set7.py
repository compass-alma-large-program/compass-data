"""
Export SerpS-18 setting 7 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1173aab_Xa09c", "uid___A002_X1173aab_Xa728"],
    field="SerpS-MM18a",
    basename="serps18-set7",
)

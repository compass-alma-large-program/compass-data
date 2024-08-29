"""
Export SVS13 setting 2 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1196e8b_Xc75b", "uid___A002_X1196e8b_Xca24"],
    field="SVS13-A",
    basename="svs13-set2",
)

"""
Export SVS13 setting 6 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1196e8b_X4c58", "uid___A002_X1196e8b_X4e35"],
    field="SVS13-A",
    basename="svs13-set6",
)

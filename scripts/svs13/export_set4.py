"""
Export SVS13 setting 4 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1107eef_Xba8c", "uid___A002_X110a1a2_X17c7f"],
    field="SVS13-A",
    basename="svs13-set4",
)

"""
Export SVS13 setting 7 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1196e8b_X5023", "uid___A002_X1196e8b_X52bc"],
    field="SVS13-A",
    basename="svs13-set7",
)

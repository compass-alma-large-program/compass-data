"""
Export IRAS4A setting 2 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1119e64_X340e", "uid___A002_X1119e64_X39af"],
    field="NGC1333_IRAS4A",
    basename="iras4a-set2",
)

"""
Export IRAS4A setting 7 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X11b41f5_X2ded", "uid___A002_X11adad7_X3bbc7"],
    field="NGC1333_IRAS4A",
    basename="iras4a-set7",
)

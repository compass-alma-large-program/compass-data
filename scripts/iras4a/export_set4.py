"""
Export IRAS4A setting 4 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X11adad7_X2d014", "uid___A002_X11adad7_X2d17e"],
    field="NGC1333_IRAS4A",
    basename="iras4a-set4",
)

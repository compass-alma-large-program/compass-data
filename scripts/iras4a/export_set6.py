"""
Export IRAS4A setting 6 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X11adad7_X34408", "uid___A002_X11adad7_X3467e"],
    field="NGC1333_IRAS4A",
    basename="iras4a-set6",
)

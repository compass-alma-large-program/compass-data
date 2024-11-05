"""
Export HOPS-373 setting 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X11b7882_X6bf7", "uid___A002_X11bcac1_X540d"],
    field="HOPS-373",
    basename="hops373-set4",
)

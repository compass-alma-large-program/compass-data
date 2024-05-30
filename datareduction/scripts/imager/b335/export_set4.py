"""
Export B335 setting 4 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1171dca_X54a3", "uid___A002_X11729b1_X5b99"],
    field="B335",
    basename="b335-set4",
)

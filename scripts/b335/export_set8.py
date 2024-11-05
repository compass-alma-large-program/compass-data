"""
Export B335 setting 8 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X11729b1_X489e", "uid___A002_X112077c_X18023"],
    field="B335",
    basename="b335-set8",
)

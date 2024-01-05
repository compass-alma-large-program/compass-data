"""
Export V883_Ori setup 9 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1020da2_X3f2f",
        "uid___A002_X10228b9_X5ff1",
    ],
    field="V883_Ori",
    basename="v883ori-set9",
)

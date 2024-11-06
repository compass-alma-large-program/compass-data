"""
Export V883_Ori setting 7 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X10275c0_X1666a",
        "uid___A002_X1036d05_X205e",
        "uid___A002_X1036d05_Xafcf",
    ],
    field="V883_Ori",
    basename="v883ori-set7",
)

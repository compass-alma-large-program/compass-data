"""
Export V883_Ori setting 1 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1020da2_Xcf27",
        "uid___A002_X10239e1_X3c21",
        "uid___A002_X112077c_X1388b",
    ],
    field="V883_Ori",
    basename="v883ori-set1",
)

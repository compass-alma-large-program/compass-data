"""
Export HOPS-108 setup 1 data to UVFITS

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
    field="HOPS-108",
    basename="hops108-set1",
)

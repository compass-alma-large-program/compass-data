"""
Export HOPS-108 setup 7 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X10275c0_X1666a",
        "uid___A002_X1036d05_X205e",
        "uid___A002_X1036d05_Xafcf",
    ],
    field="HOPS-108",
    basename="hops108-set7",
)

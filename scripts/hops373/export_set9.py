"""
Export HOPS-373 setting 9 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1020da2_X3f2f",
        "uid___A002_X10228b9_X5ff1",
    ],
    field="HOPS-373",
    basename="hops373-set9",
)

"""
Export HOPS-108 setting 9 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X1020da2_X3f2f",
        "uid___A002_X10228b9_X5ff1",
    ],
    field="HOPS-108",
    basename="hops108-set9",
)

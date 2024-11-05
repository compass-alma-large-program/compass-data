"""
Export HOPS-373 setting 8 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X101e5ab_X316b",
        "uid___A002_X1020da2_X340c",
    ],
    field="HOPS-373",
    basename="hops373-set8",
)

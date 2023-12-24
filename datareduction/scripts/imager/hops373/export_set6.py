"""
Export HOPS-373 setup 6 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1020da2_Xd807",
        "uid___A002_X10239e1_Xbf2b",
        "uid___A002_X10239e1_Xd3ac",
    ],
    field="HOPS-373",
    basename="hops373-set6",
)

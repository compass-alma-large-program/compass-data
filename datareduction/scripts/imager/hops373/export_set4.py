"""
Export HOPS-373 setup 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1128118_Xd51", "uid___A002_X1128118_X1555"],
    field="HOPS-373",
    basename="hops373-set4",
)

"""
Export V883_Ori setting 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1128118_Xd51", "uid___A002_X1128118_X1555"],
    field="V883_Ori",
    basename="v883ori-set4",
)

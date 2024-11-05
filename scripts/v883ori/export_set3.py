"""
Export V883_Ori setting 3 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1128118_X1dfd",
        "uid___A002_X1171dca_X654a",
        "uid___A002_X1178b24_X3d1c",
    ],
    field="V883_Ori",
    basename="v883ori-set3",
)

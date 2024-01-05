"""
Export V883_Ori setup 8 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X101e5ab_X316b",
        "uid___A002_X1020da2_X340c",
    ],
    field="V883_Ori",
    basename="v883ori-set8",
)

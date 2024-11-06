"""
Export V883_Ori setting 2 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X117d38c_X43bc",
        "uid___A002_X112077c_X2efec",
        "uid___A002_X112077c_X13ef2",
    ],
    field="V883_Ori",
    basename="v883ori-set2",
)

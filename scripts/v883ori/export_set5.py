"""
Export V883_Ori setting 5 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X1038a19_X2369",
        "uid___A002_X112077c_X14637",
        "uid___A002_X112077c_X1cd7c",
    ],
    field="V883_Ori",
    basename="v883ori-set5",
)

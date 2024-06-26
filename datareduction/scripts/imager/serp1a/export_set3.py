"""
Export Serp-1a setting 3 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X117d38c_X17cb",
        "uid___A002_X117d38c_X87e1",
        "uid___A002_X117d38c_Xec1e",
    ],
    field="Serp_SMM1-a",
    basename="serp1a-set3",
)

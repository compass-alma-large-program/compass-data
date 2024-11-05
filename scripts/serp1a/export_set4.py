"""
Export Serp-1a setting 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X117a165_X508e",
        "uid___A002_X117a165_X4143",
        "uid___A002_X1175218_Xa35c",
    ],
    field="Serp_SMM1-a",
    basename="serp1a-set4",
)

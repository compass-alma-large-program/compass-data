"""
Export SerpS-18 setting 4 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X117a165_X508e",
        "uid___A002_X117a165_X4143",
        "uid___A002_X1175218_Xa35c",
    ],
    field="SerpS-MM18a",
    basename="serps18-set4",
)

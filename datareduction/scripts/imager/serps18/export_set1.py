"""
Export SerpS-18 setting 1 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1175218_X1092a",
        "uid___A002_X117a165_X3995",
        "uid___A002_X117a165_X489f",
    ],
    field="SerpS-MM18a",
    basename="serps18-set1",
)

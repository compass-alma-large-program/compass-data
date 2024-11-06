"""
Export SerpS-18 setting 8 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X9c02", "uid___A002_X1175218_X945d"],
    field="SerpS-MM18a",
    basename="serps18-set8",
)

"""
Export SerpS-18 setting 6 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X4443", "uid___A002_X1175218_X3e66"],
    field="SerpS-MM18a",
    basename="serps18-set6",
)

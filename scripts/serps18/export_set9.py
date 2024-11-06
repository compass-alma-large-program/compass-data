"""
Export SerpS-18 setting 9 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X3763", "uid___A002_X1173aab_X9768"],
    field="SerpS-MM18a",
    basename="serps18-set9",
)

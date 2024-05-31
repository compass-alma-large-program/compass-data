"""
Export Serp-1a setting 6 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1175218_X4443", "uid___A002_X1175218_X3e66"],
    field="Serp_SMM1-a",
    basename="serp1a-set6",
)

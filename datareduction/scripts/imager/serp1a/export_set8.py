"""
Export Serp-1a setting 8 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1175218_X9c02", "uid___A002_X1175218_X945d"],
    field="Serp_SMM1-a",
    basename="serp1a-set8",
)

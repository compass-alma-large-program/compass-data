"""
Export Serp-1a setting 9 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1175218_X3763", "uid___A002_X1173aab_X9768"],
    field="Serp_SMM1-a",
    basename="serp1a-set9",
)

"""
Export Serp-1a setting 2 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X117bb05_X8747", "uid___A002_X117bb05_X8142"],
    field="Serp_SMM1-a",
    basename="serp1a-set2",
)

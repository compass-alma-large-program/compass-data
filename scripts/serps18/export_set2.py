"""
Export SerpS-18 setting 2 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X117bb05_X8747", "uid___A002_X117bb05_X8142"],
    field="SerpS-MM18a",
    basename="serps18-set2",
)

"""
Export HOPS-373 setting 5 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X1038a19_X2369",
        "uid___A002_X112077c_X14637",
        "uid___A002_X112077c_X1cd7c",
    ],
    field="HOPS-373",
    basename="hops373-set5",
)

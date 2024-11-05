"""
Export HOPS-108 setting 3 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=[
        "uid___A002_X1128118_X1dfd",
        "uid___A002_X1171dca_X654a",
        "uid___A002_X1178b24_X3d1c",
    ],
    field="HOPS-108",
    basename="hops108-set3",
)

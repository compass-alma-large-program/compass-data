"""
Export SVS13 setting 5 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1198c0c_X3818", "uid___A002_X1198c0c_X3a27"],
    field="SVS13-A",
    basename="svs13-set5",
)

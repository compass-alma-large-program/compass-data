"""
Export SVS13 setting 9 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(uid="uid___A002_X110a1a2_X24ff", field="SVS13-A", basename="svs13-set9")

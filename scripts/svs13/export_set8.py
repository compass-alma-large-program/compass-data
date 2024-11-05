"""
Export SVS13 setting 8 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(uid="uid___A002_X1107eef_Xc183", field="SVS13-A", basename="svs13-set8")

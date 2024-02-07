"""
Export SVS13 setting 3 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(uid="uid___A002_X110a1a2_X20527", field="SVS13-A", basename="svs13-set3")

"""
Export B335 setting 9 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid="uid___A002_X1171dca_X4db5", field="B335", basename="b335-set9")

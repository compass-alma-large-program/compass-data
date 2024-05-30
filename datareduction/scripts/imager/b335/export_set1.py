"""
Export B335 setting 1 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X11729b1_X4ea6", field = "B335", basename = "b335-set1")

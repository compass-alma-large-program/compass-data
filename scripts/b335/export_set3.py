"""
Export B335 setting 3 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X11729b1_X54b4", field = "B335", basename = "b335-set3")

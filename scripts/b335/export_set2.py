"""
Export B335 setting 2 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X105715f_X1db7", field = "B335", basename = "b335-set2")

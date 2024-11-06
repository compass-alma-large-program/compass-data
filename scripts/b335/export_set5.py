"""
Export B335 setting 5 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X1035744_Xffaa", field = "B335", basename = "b335-set5")

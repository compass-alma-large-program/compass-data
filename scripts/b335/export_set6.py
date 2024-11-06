"""
Export B335 setting 6 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X1036d05_X4eca", field = "B335", basename = "b335-set6")

"""
Export B335 setting 7 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X1036d05_X5223", field = "B335", basename = "b335-set7")

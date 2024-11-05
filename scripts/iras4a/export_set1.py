"""
Export IRAS4A setting 1 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X101e5ab_Xcd8", field = "NGC1333_IRAS4A", basename = "iras4a-set1")

"""
Export BHR71 setting 2 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X101c3b2_Xc445", field = "BHR71-IRS1", basename = "bhr71-set2")

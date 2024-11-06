"""
Export BHR71 setting 1 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X101c3b2_Xbcf0", field = "BHR71-IRS1", basename = "bhr71-set1")

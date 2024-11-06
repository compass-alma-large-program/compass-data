"""
Export BHR71 setting 8 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X10275c0_Xf606", field = "BHR71-IRS1", basename = "bhr71-set8")

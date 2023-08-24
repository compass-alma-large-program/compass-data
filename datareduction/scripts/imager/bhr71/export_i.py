"""
Export BHR71 I setup data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X10275c0_Xfe27", field = "BHR71-IRS1", basename = "bhr71-i")

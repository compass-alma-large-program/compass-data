"""
Export BHR71 B setup data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X101c3b2_Xc445", field = "BHR71-IRS1", basename = "bhr71-b")

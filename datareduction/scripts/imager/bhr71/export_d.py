"""
Export BHR71 D setup data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X10239e1_X5b1c", field = "BHR71-IRS1", basename = "bhr71-d")

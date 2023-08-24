"""
Export BHR71 G setup data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X10239e1_Xfbe7", field = "BHR71-IRS1", basename = "bhr71-g")

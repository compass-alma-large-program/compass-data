"""
Export BHR71 C setup data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X10228b9_X7050", field = "BHR71-IRS1", basename = "bhr71-c")

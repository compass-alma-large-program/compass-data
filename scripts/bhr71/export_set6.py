"""
Export BHR71 setting 6 data to UVFITS

"""

import sys
sys.path.append("../lib")
from export import export

export(uid = "uid___A002_X10239e1_X6090", field = "BHR71-IRS1", basename = "bhr71-set6")

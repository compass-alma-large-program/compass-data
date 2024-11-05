"""
Export BHR71 setting 3 data to UVFITS

"""

import sys
sys.path.append("../common")
from export import export

export(uid = "uid___A002_X10228b9_X7050", field = "BHR71-IRS1", basename = "bhr71-set3")

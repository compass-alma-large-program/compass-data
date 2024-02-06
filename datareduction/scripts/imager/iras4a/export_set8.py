"""
Export IRAS4A setting 8 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(uid="uid___A002_X1115718_X262ab", field="NGC1333_IRAS4A", basename="iras4a-set8")

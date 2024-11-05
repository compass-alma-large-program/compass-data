"""
Export IRAS4A setting 3 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(uid="uid___A002_X1115718_X1a40e", field="NGC1333_IRAS4A", basename="iras4a-set3")

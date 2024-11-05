"""
Export L1551-IRS5 setting 6 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(uid="uid___A002_X110a1a2_X21b6b", field="L1551_IRS_5", basename="l1551irs5-set6")

"""
Export L1551-IRS5 setting 5 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(uid="uid___A002_X1198c0c_Xc6f1", field="L1551_IRS_5", basename="l1551irs5-set5")

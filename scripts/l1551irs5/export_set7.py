"""
Export L1551-IRS5 setting 7 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(uid="uid___A002_X1198c0c_X4dae", field="L1551_IRS_5", basename="l1551irs5-set7")

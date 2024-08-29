"""
Export L1551-IRS5 setting 8 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X11a1c8d_X11681", "uid___A002_X1198c0c_Xd56a"],
    field="L1551_IRS_5",
    basename="l1551irs5-set8",
)

"""
Export L1551-IRS5 setting 4 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1193ccc_X1b8dd", "uid___A002_X1196e8b_Xcc19"],
    field="L1551_IRS_5",
    basename="l1551irs5-set4",
)

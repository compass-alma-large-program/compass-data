"""
Export L1551-IRS5 setting 3 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=["uid___A002_X1196e8b_Xe5cd", "uid___A002_X1198c0c_X4076"],
    field="L1551_IRS_5",
    basename="l1551irs5-set3",
)

"""
Export L1551-IRS5 setting 1 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    uid=["uid___A002_X1196e8b_X5891", "uid___A002_X1196e8b_Xd9bd"],
    field="L1551_IRS_5",
    basename="l1551irs5-set1",
)

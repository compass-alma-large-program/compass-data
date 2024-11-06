"""
Export IRAS4A setting 5 data to UVFITS

"""

import sys

sys.path.append("../common")
from export import export

export(
    # The frequency coverage for the second EB seem incorrect. Ignore it for the moment.
    #uid=["uid___A002_X11adad7_X3b9a1", "uid___A002_X112077c_X1bb87"],
    uid="uid___A002_X11adad7_X3b9a1",
    field="NGC1333_IRAS4A",
    basename="iras4a-set5",
)

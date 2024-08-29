"""
Export SerpS-18 setting 5 data to UVFITS

"""

import sys

sys.path.append("../lib")
from export import export

export(
    uid=[
        "uid___A002_X117d38c_X203f9",
        "uid___A002_X11adad7_X1c75d",
    ],
    field="SerpS-MM18a",
    basename="serps18-set5",
)

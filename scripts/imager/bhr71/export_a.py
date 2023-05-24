"""
Export the MS data to UVFITS

"""

import os
import glob
import shutil

basename = "bhr71-a"
datadir = "../../../data/calibrated/"
inputdir = os.path.realpath(datadir + "/ms")
outputdir = os.path.realpath(datadir + "/uvfits")
__rethrow_casa_exceptions = True

# Extract the data

os.chdir(inputdir)

shutil.rmtree(basename + ".ms", ignore_errors=True)

split(
    vis="uid___A002_X101c3b2_Xbcf0.ms.split.cal",
    outputvis=basename + ".ms",
    datacolumn="data",
    intent="OBSERVE_TARGET#ON_SOURCE",
    field="BHR71-IRS1",
    spw="25,27,29,31",
    keepflags=False,
)

# Convert the velocity frame to LSR

shutil.rmtree(basename + "-cvel.ms", ignore_errors=True)

cvel2(
    vis=basename + ".ms",
    outputvis=basename + "-cvel.ms",
    spw="0,1,2,3",
    outframe="LSRK",
)

# Export the MS to UVFITS

exportuvfits(
    vis=basename + "-cvel.ms",
    fitsfile=basename + ".uvfits",
    datacolumn="data",
    multisource=False,
    overwrite=True,
)

# Move the file to the output directory

try:
    os.remove(outputdir + "/" + basename + ".uvfits")
except OSError:
    pass
shutil.move(basename + ".uvfits", outputdir)

# Remove intermediate files and CASA logs

shutil.rmtree(basename + ".ms", ignore_errors=True)
shutil.rmtree(basename + "-cvel.ms", ignore_errors=True)
for f in glob.glob("*.last"):
    os.remove(f)

"""
Export the MS data to UVFITS

"""

import os
import glob
import shutil
import tarfile
import casatasks as ct


def export(uid, field, basename):
    """
    Export the MS data to UVFITS

    Parameters
    ----------
    uid : str
        The UID of the dataset
    field : str
        The name of the field
    basename : str
        The basename of the output file

    """

    spws = [25, 27, 29, 31]
    datadir = "../../../../data/calibrated/"
    inputdir = os.path.realpath(datadir + "/ms")
    outputdir = os.path.realpath(datadir + "/uvfits")

    __rethrow_casa_exceptions = True

    os.chdir(inputdir)

    # Untar the file

    with tarfile.open(uid + ".ms.split.cal.tar") as tar:
        tar.extractall()

    for spw in spws:
        name = basename + "-spw%i" % spw

        # Extract the data

        shutil.rmtree(name + ".ms", ignore_errors=True)
        ct.split(
            vis=uid + ".ms.split.cal",
            outputvis=name + ".ms",
            datacolumn="data",
            intent="OBSERVE_TARGET#ON_SOURCE",
            field=field,
            spw="%i" % spw,
            keepflags=False,
        )

        # Convert the velocity frame to LSR

        shutil.rmtree(name + "-cvel.ms", ignore_errors=True)
        ct.cvel2(
            vis=name + ".ms",
            outputvis=name + "-cvel.ms",
            outframe="LSRK",
        )

        # Export the MS to UVFITS

        ct.exportuvfits(
            vis=name + "-cvel.ms",
            fitsfile=name + ".uvfits",
            datacolumn="data",
            multisource=False,
            overwrite=True,
        )

        # Move the file to the output directory

        try:
            os.remove(outputdir + "/" + name + ".uvfits")
        except OSError:
            pass
        shutil.move(name + ".uvfits", outputdir)

        # Remove intermediate files

        shutil.rmtree(name + ".ms", ignore_errors=True)
        shutil.rmtree(name + "-cvel.ms", ignore_errors=True)

    # Remove CASA logs

    for f in glob.glob("*.last"):
        os.remove(f)

    # Remove the untarred directory

    shutil.rmtree(uid + ".ms.split.cal", ignore_errors=True)

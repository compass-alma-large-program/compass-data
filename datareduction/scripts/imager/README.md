Data reduction scripts for IMAGER using pipeline steps

Prerequisites:
IMAGER (>= 3.9-05)
CASA (>= 6.5.6.22)

Getting the calibrated visibilities and converting them to UVFITS:

1. Put the measurement set in the working directory. Untar it if it is tared. This takes less than an hour.

2. IMAGER cannot work with CASA measurement sets directly. It works on UVFITS files that need to be extracted from the measurement set. 
This is done in three steps in CASA:

CASA <1>: vis = 'uid___A002_X10275c0_Xfe27.ms.split.cal'
CASA <2>: casagildas()
CASA <3>: casagildas("Do")

This takes less then an hour.
The four spectral windows of the target source are extracted automatically and stored in four UVFITS files in the working directory.
The UVFITS files are automatically named SOURCE-FREQUENCY.uvfits with SOURCE the target source name in the measurement set and FREQUENCY
the central frequency of the spectral window.

Running the IMAGER script:

1. Put myimager.ima and proc_myimager.ima in the working directory
2. Start IMAGER
3. Execute in IMAGER:

@ myimager.ima

This will take about one hour.

What myimager.ima does:

The script organizes the working directory by automatically creating folders named UVFITS/, RAW/, SELF/, MAPS/, FITS/.
It moves the UVFITS files into UVFITS/. 
RAW/ will contain the UV tables (in GILDAS format). 
SELF/ will contain the processed UV tables (with self-cal or not. A prefix s- in the filenames will indicate if self-cal was applied or not).
MAPS/ will contain the deconvolved images and cubes in GILDAS format
FITS/ will contain the deconvolved images and cubes in FITS format

The script evaluates if self-cal is useful or not and computes it if needed. It then performs the deconvolution. The splitting between lines and continuum
is done only at the end, after imaging. The scripts produces both files that are not corrected for the primary beam response (lmv-clean files in MAPS/) 
and files that are corrected for it (lmv-sky files in MAPS). In the FITS/ folder, the files corrected for primary beam response are labeled _pbcor.
In both MAPS/ and FITS/ the files labeled _c are the continuum images and the files labeled _l are the continuum-free line cubes.

The user can impose many parameters in IMAGER. In the current version of myimager.ima, the user can:
. decide or not to apply self-cal (parameter myDoSelfCal)
. impose or not the map size and pixel size (parameters mySetSizes, mysize, mycell)
. impose or not the robust parameter (parameters mYSetRobust, mymrob). A value of -1.5 correspond to robust = 0.5 in CASA (see IMAGER documentation).
. choose the method used to split line and continuum. In the current version, it is set to C-SCM (see IMAGER documentation for other methods).

The line starting with !let all%phase_times can be uncommented if the user wants to test the impact of changing the averaging time for the phase self-cal for
instance.

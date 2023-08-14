## Run this script after scriptForReprocessing_COMPASS.py
## We want to restart TCLEAN where ph03 stopped
## Manual editing will be needed, and will be marked 
## You can run it like: /opt/local/bin/mpicasa -n 8 /opt/local/bin/casa-alma --pipeline -c scriptForPhase04_COMPASS.py ???
## casa-alma --pipeline -c scriptForPhase04_COMPASS.py

import shutil
import os
import sys
import re
import glob


####################
#### INPUT PARAMETERS IF NEEDED
####################

workingDirectory = '/lustre/cv/projects/COMPASS/aplunkett/BHR71-IR_a_07_TM1/working/calibrated_final/'
visname = workingDirectory+'measurement_sets/uid___A002_X101c3b2_Xbcf0_targets_line.ms' ## 
outImageDirectory = workingDirectory+'modified_images_folder_ph04/' ## Specify where you want your output images to go

doSetup = True #this is set as True the first time if you need to setup the files in proper places
makeFits = True #this is set as True if you want to make FITS files from CASA images
####################

####################
#### FUNCTIONS, DO NOT EDIT
####################

def setup_to_copy():
    os.mkdir('working_reprocess_ph04')
    files = glob.glob('images_contsub/*spw*.cube.I.iter1.*') ## check that the directory is correct
    for ff in files:
        filename = ff.split('/')[1] #get just the filename after the directory name (separated by /)
        newfilename = re.sub('iter1','iter2',filename) #replace iter1 with iter2 in the filename
        shutil.copytree(src=ff,dst='working_reprocess_ph04/'+newfilename) #make a copy and call it by newfilename
        
####################


####################
## First, copy the *.iter1* files
## To a directory working_reprocess_ph04
####################

if doSetup: 
    print('doing setup')
    setup_to_copy()

os.chdir('working_reprocess_ph04/')

####################
## Resume TCLEAN
####################

## Now we are in the /working_reprocess_ph04 directory
## and working with iter2 files

## COPY THE LAST 4 TCLEAN COMMANDS FROM casa_commands.log
## There should be one for each SPW
## Make sure niter!=0 (otherwise you have the wrong command)

## EDIT/CHECK ALL 4 FOLLOWING TCLEAN COMMANDS
## Make these changes:
#[0] vis=[visname]
#[1] imagename='' should end with iter2, not iter1
#[2] threshold=newthreshold (which is set to '0.0038Jy')
#[3] edit start= with correct start Frequency (from weblog)
#[4] check antenna list (from weblog)
#[5] check scan numbers (from weblog)
#[6] If there is a line break in phasecenter, remove the break, otherwise you will get an EOL error.  It should look like phasecenter='ICRS 12:01:36.4988 -065.08.49.381' (with correct coordinates)

newthreshold='0.0038Jy'

tclean(vis=visname, field='BHR71-IRS1', ## EDIT THIS LINE with vis=visname
       spw=['25'],
       antenna=['0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41&'], ## CHECK THIS LINE
       scan=['8,12,16,20,24,28'], intent='OBSERVE_TARGET#ON_SOURCE', ## CHECK THIS LINE
       datacolumn='data',
       imagename='oussid.s10_0.BHR71-IRS1_sci.spw25.cube.I.iter2', imsize=[500, ## EDIT THIS LINE with correct SPW
       500], cell=['0.064arcsec'], phasecenter='ICRS 12:01:36.4988 -065.08.49.381', stokes='I', specmode='cube', nchan=3837,
       start='279.0475460151GHz', width='0.2441427MHz', outframe='LSRK', ## EDIT THIS LINE with correct start=''
       perchanweightdensity=True, gridder='standard', mosweight=False,
       usepointing=False, pblimit=0.2, deconvolver='hogbom', restoration=True,
       restoringbeam='common', pbcor=True, weighting='briggsbwtaper',
       robust=0.5, npixels=0, niter=1000000, threshold=newthreshold, nsigma=0.0, ## EDIT THIS LINE to use threshold=newthreshold
       interactive=0, usemask='auto-multithresh', sidelobethreshold=2.0,
       noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=7.0,
       minbeamfrac=0.3, growiterations=50, dogrowprune=True,
       minpercentchange=1.0, fastnoise=False, restart=True, savemodel='none',
       calcres=False, calcpsf=False, parallel=True)

tclean(vis=visname, field='BHR71-IRS1',
       spw=['27'],
       antenna=['0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41&'],
       scan=['8,12,16,20,24,28'], intent='OBSERVE_TARGET#ON_SOURCE',
       datacolumn='data',
       imagename='oussid.s10_0.BHR71-IRS1_sci.spw27.cube.I.iter2', imsize=[500,
       500], cell=['0.064arcsec'], phasecenter='ICRS 12:01:36.4988 -065.08.49.381', stokes='I', specmode='cube', nchan=3837,
       start='279.9550542895GHz', width='0.2441427MHz', outframe='LSRK',
       perchanweightdensity=True, gridder='standard', mosweight=False,
       usepointing=False, pblimit=0.2, deconvolver='hogbom', restoration=True,
       restoringbeam='common', pbcor=True, weighting='briggsbwtaper',
       robust=0.5, npixels=0, niter=1000000, threshold=newthreshold, nsigma=0.0,
       interactive=0, usemask='auto-multithresh', sidelobethreshold=2.0,
       noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=7.0,
       minbeamfrac=0.3, growiterations=50, dogrowprune=True,
       minpercentchange=1.0, fastnoise=False, restart=True, savemodel='none',
       calcres=False, calcpsf=False, parallel=True)

tclean(vis=visname, field='BHR71-IRS1',
       spw=['29'],
       antenna=['0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41&'],
       scan=['8,12,16,20,24,28'], intent='OBSERVE_TARGET#ON_SOURCE',
       datacolumn='data',
       imagename='oussid.s10_0.BHR71-IRS1_sci.spw29.cube.I.iter2', imsize=[500,
       500], cell=['0.064arcsec'], phasecenter='ICRS 12:01:36.4988 -065.08.49.381', stokes='I', specmode='cube', nchan=3838,
       start='280.8625898094GHz', width='0.2441427MHz', outframe='LSRK',
       perchanweightdensity=True, gridder='standard', mosweight=False,
       usepointing=False, pblimit=0.2, deconvolver='hogbom', restoration=True,
       restoringbeam='common', pbcor=True, weighting='briggsbwtaper',
       robust=0.5, npixels=0, niter=3000000, threshold=newthreshold, nsigma=0.0,
       interactive=0, usemask='auto-multithresh', sidelobethreshold=2.0,
       noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=7.0,
       minbeamfrac=0.3, growiterations=50, dogrowprune=True,
       minpercentchange=1.0, fastnoise=False, restart=True, savemodel='none',
       calcres=False, calcpsf=False, parallel=True)

tclean(vis=visname, field='BHR71-IRS1',
       spw=['31'],
       antenna=['0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41&'],
       scan=['8,12,16,20,24,28'], intent='OBSERVE_TARGET#ON_SOURCE',
       datacolumn='data',
       imagename='oussid.s10_0.BHR71-IRS1_sci.spw31.cube.I.iter2', imsize=[500,
       500], cell=['0.064arcsec'], phasecenter='ICRS 12:01:36.4988 -065.08.49.381', stokes='I', specmode='cube', nchan=3838,
       start='281.7700748225GHz', width='0.2441428MHz', outframe='LSRK',
       perchanweightdensity=True, gridder='standard', mosweight=False,
       usepointing=False, pblimit=0.2, deconvolver='hogbom', restoration=True,
       restoringbeam='common', pbcor=True, weighting='briggsbwtaper',
       robust=0.5, npixels=0, niter=1000000, threshold=newthreshold, nsigma=0.0,
       interactive=0, usemask='auto-multithresh', sidelobethreshold=2.0,
       noisethreshold=5.0, lownoisethreshold=1.5, negativethreshold=7.0,
       minbeamfrac=0.3, growiterations=50, dogrowprune=True,
       minpercentchange=1.0, fastnoise=False, restart=True, savemodel='none',
       calcres=False, calcpsf=False, parallel=True)

####################
## Move images to outpImageDirectory
####################

## First check if that directory exists
if not glob.glob(outImageDirectory):
        # make directory to move images to
        os.mkdir(outImageDirectory)
else:
        print('ERROR: images directory "'+outImageDirectory+'" already exists. Will not overwrite. Please specify a new folder name at the start of the script; then just copy-paste the final lines to copy.')
        sys.exit()


## Then make the move

os.system("mv *.image "+outImageDirectory+" 2> /dev/null")
os.system("mv *.image.pbcor "+outImageDirectory+" 2> /dev/null")
os.system("mv *.mask "+outImageDirectory+" 2> /dev/null")
os.system("mv *.mask.flattened "+outImageDirectory+" 2> /dev/null")
os.system("mv *.model "+outImageDirectory+" 2> /dev/null")
os.system("mv *.pb "+outImageDirectory+" 2> /dev/null")
os.system("mv *.psf "+outImageDirectory+" 2> /dev/null")
os.system("mv *.residual "+outImageDirectory+" 2> /dev/null")
os.system("mv *.sumwt "+outImageDirectory+" 2> /dev/null")

####################
## While in CASA, option to make FITS files from CASA image formats
## Move the FITS files into the directory called toERDA, 
## This makes it easier to then upload them to a central location (ERDA)
####################

if makeFits:
    ## Make, and navigate to a directory called toERDA
    os.system("mkdir toERDA")
    os.chdir('toERDA')
    ## Identify the directories for Phases 1, 3, 4
    ph01dir = workingDirectory+'modified_images_folder_ph01/'
    ph03dir = workingDirectory+'modified_images_folder_ph03/'
    ph04dir = outImageDirectory
    ## Move cubes from each phase,  and one  continuum image
    for file in glob.glob(ph01dir+'*cube.I.iter1.image.pbcor'):
        print('#### making FITS file for: \n'+file)
        exportfits(imagename=file,fitsimage=file+'.fits')
    for file in glob.glob(ph03dir+'*cube.I.iter1.image.pbcor'):
        print('#### making FITS file for: \n'+file)
        exportfits(imagename=file,fitsimage=file+'.fits')
    for file in glob.glob(ph03dir+'*cont.I.iter1.image.pbcor'):
        print('#### making FITS file for: \n'+file)
        exportfits(imagename=file,fitsimage=file+'.fits')
    for file in glob.glob(ph04dir+'*cube.I.iter2.image.pbcor'):
        print('#### making FITS file for: \n'+file)
        exportfits(imagename=file,fitsimage=file+'.fits')
    ## These next lines move the fits files into the toERDA directory
    os.system('mv '+ph01dir+'*cube.I.iter1.image.pbcor.fits .')
    os.system('mv '+ph03dir+'*cube.I.iter1.image.pbcor.fits .')
    os.system('mv '+ph03dir+'*cont.I.iter1.image.pbcor.fits .')
    os.system('mv '+ph04dir+'*cube.I.iter2.image.pbcor.fits .')

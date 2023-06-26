## COMPASS Data Reduction
## Script to rerun the pipeline steps in Phase 3
## Includes continuum subtraction and imaging
## Author: Adele Plunkett, 2023-05-30

import glob as glob
__rethrow_casa_exceptions=True
pipelinemode='automatic'

#### THIS LINE SHOULD BE CONSISTENT WITH  THE FIRST RUN.
#### You should work with a COPY of the data in your working directory, and not the "original" version.
MyVisName = 'uid___A002_X101c3b2_Xbcf0.ms.split.cal'
MyDirName =  '/lustre/cv/projects/COMPASS/aplunkett/BHR71-IR_a_07_TM1/'
####
####

#### Possible user input, for DR to check:
MyRobust = 0.5
MySPW = '' ## this should be '' (empty) if all SPWs have changes and/or should be imaged again, and if you want aggregate continuum
#### 

#### Remove some files from this space if you ran previously 
#### (copy these elsewhere if you need them later for reference)
os.system('rm -rf calibrated_targets* ')

#### ALP 2023-06-20
#### This is a necessary step due to being delivered the .split.cal and needing the .ms file for the pipeline run
#### You can comment this line if you already did it once.
clearcal(vis=MyDirName+MyVisName)
os.system('mv '+MyVisName+' calibrated.ms')

MyNewVis = 'calibrated.ms'

#### PL Commands

context = h_init()
context.project_summary.proposal_code = 'NEW CONTSUB'
try:
    hifa_importdata(vis=MyNewVis,dbservice=False,pipelinemode=pipelinemode) ##ALP 2023-03-20: added here
    ## Split science targets and apply flags
    hif_mstransform(pipelinemode=pipelinemode) ##ALP 2023-06-15 Added because .split.cal was being deleted, not sure why.
    hifa_flagtargets(pipelinemode=pipelinemode)
    ## ALP Removed lines hifa_imageprecheck and hif_checkproductsize
    ## Fit and subtract the continuum using revised cont.dat for all spws
    hif_makeimlist(specmode='mfs',robust=MyRobust,spw=MySPW)
    hif_uvcontfit(pipelinemode=pipelinemode)
    hif_uvcontsub(pipelinemode=pipelinemode)
    hif_makeimages(pipelinemode=pipelinemode)

    ## Make new aggregate cont (if no individual SPW is selected)
    if MySPW == '':
        hif_makeimlist(specmode='cont',robust=MyRobust,pipelinemode=pipelinemode) 
        hif_makeimages(pipelinemode=pipelinemode)    

    ## Make new continuum subtracted cube for revised spw(s)
    hif_makeimlist(specmode='cube',robust=MyRobust,spw=MySPW,pipelinemode=pipelinemode) 
    hif_makeimages(pipelinemode=pipelinemode)

    hifa_exportdata(pipelinemode=pipelinemode,imaging_products_only=True)
finally:
    h_save()

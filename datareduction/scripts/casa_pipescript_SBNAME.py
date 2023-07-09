import glob as glob
__rethrow_casa_exceptions=True
pipelinemode='automatic'

#### THIS IS THE ONLY LINE YOU SHOULD NEED TO EDIT
#### FOR THE FIRST RUN.
MyVis = glob.glob('/PATH/TO/calibrated/*.ms.split.cal') 
####
####

MyRobust = 0.5
context = h_init()
try:
    hifa_importdata(vis=MyVis,dbservice=False) ##ALP 2023-03-20: added here
    hif_mstransform(pipelinemode="automatic") ##ALP 2023-03-20: Not necessary??
    hifa_flagtargets(pipelinemode="automatic")
    ##hifa_imageprecheck(pipelinemode="automatic") ##ALP 2023-03-20: Run this IF anything strange in initial run
    hif_makeimlist(specmode='mfs',robust=MyRobust)
    hif_makeimages(pipelinemode="automatic")
    hif_makeimlist(specmode='cont',robust=MyRobust)
    hif_makeimages(pipelinemode="automatic")
    hif_makeimlist(specmode='cube',robust=MyRobust)
    hif_makeimages(pipelinemode="automatic")
    hifa_exportdata(imaging_products_only=True)
finally:
    h_save()

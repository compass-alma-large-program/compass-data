# run this script within the working/ directory to create a calibrated_final/ directory, mirroring the NA added value delivery structure.
# once calibrated_final/ is created, place scriptForReprocessing.py in calibrated_final/ and follow the scriptForReprocessing.py instructions

import glob
import os
import sys

#################
### THIS IS THE ONLY INFORMATION YOU SHOULD PROVIDE...
#################
MyUid = 'uid___A002_X101c3b2_Xbcf0'
MyVisName = MyUid+'.ms.split.cal'
MyDirName =  '/lustre/cv/projects/COMPASS/aplunkett/BHR71-IR_a_07_TM1/'
#################
#################


### SPLIT OFF SCIENCE TARGET DATA
sourcevis='calibrated_targets.ms'
rmtables(sourcevis)
os.system('rm -rf ' + sourcevis + '.flagversions')
split(vis=MyDirName+MyVisName,
  intent='*TARGET*', # split off the target sources, to be certain
  outputvis=sourcevis,
  datacolumn='data') #get data in 'data' column

### GET THE DATA INTO THE FORMAT THAT THE PIPELINE EXPECTS
clearcal(vis='calibrated_targets.ms')
os.system('mv calibrated_targets.ms '+MyUid+'_targets.ms') #rename to have the name of the MyUID

MyNewVis = MyUid+'_targets.ms'

### THIS IS WHERE THE reprocessing_prep.py resumes

# Check if calibrated_final/ already exists:
if glob.glob("calibrated_final"):
    print("ERROR: calibrated_final/ already exists; will not overwrite")
    sys.exit()
else:
    os.mkdir("calibrated_final")

# Fill the caltables -- ONLY if you have done Ph03 before.
os.mkdir("calibrated_final/caltables")
os.system("cp -rf cont.dat calibrated_final/caltables") ## If you already have done the Ph03 step, then put the cont.dat file in caltables/
os.system("cp -rf *uvcont.tbl calibrated_final/caltables")

# Fill the measurement_sets
os.mkdir("calibrated_final/measurement_sets")
# First try just uid*targets.ms
os.system("cp -rf uid*targets.ms calibrated_final/measurement_sets/")
# Then try uid*targets_line.ms -- BUT, if you have not done Ph03 before, this won't exist
os.system("cp -rf uid*targets_line.ms calibrated_final/measurement_sets/")

print("Generated calibrated_final/ and filled caltables/ and measurement_sets/. Please place scriptForReprocessing.py in calibrated_final/ and follow README instructions.")


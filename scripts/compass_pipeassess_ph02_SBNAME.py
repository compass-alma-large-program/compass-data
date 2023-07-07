### This is a script for inspecting the COMPASS pipeline run, Phase 1
### EXAMPLE: BHR71-IR_a_07_TM1
### Phase 1:  running the imaging pipeline WITHOUT continuum subtraction
### You should be working in the /working/ directory
### output images were:
#oussid.s9_0.BHR71-IRS1_sci.spw25.cube.I.iter1.image.pbcor/
#oussid.s9_0.BHR71-IRS1_sci.spw27.cube.I.iter1.image.pbcor/
#oussid.s9_0.BHR71-IRS1_sci.spw29.cube.I.iter1.image.pbcor/
#oussid.s9_0.BHR71-IRS1_sci.spw31.cube.I.iter1.image.pbcor/

import glob as glob
import numpy as np
import matplotlib.pyplot as plt

## target name here should match the text in the image name
targetname = 'BHR71-IRS1'

## define the region for extracting the spectrum
## default: 'center' (10x10 pixels box); allowed: 'masked_region', 'center'
region = 'center'

## image list of all SPWs
imlist = glob.glob('*.'+targetname+'_sci.*.cube.I.iter1.image.pbcor')
## list of mask images (if needed for assessment)
masklist = glob.glob('*.'+targetname+'_sci.*.cube.I.iter1.mask')

## Get image dimensions and center pixel
imsizex = imhead(imlist[0])['shape'][0]
imsizey = imhead(imlist[0])['shape'][1]
ctrx = int(imsizex/2)
ctry = int(imsizey/2)
## Generate a string that represents a box at the center with size
## 10x10 pixels
blcx = ctrx-5
blcy = ctry-5
trcx = ctrx+5
trcy = ctry+5
boxstr = str(blcx) + ','+str(blcy)+','+str(trcx)+','+str(trcy)

## Write out the spectrum in the masked region of the image for each SPW
for ii in np.arange(np.size(imlist)):
    if region == 'center':
        specflux(imagename=imlist[ii], unit="GHz", logfile=imlist[ii]+".spec.txt",box=boxstr,overwrite=True)
    elif region == 'masked_region'
        specflux(imagename=imlist[ii], unit="GHz", logfile=imlist[ii]+".spec.txt",mask=f"mask({masklist[ii]})",overwrite=True)
    f = open(imlist[ii]+".spec.txt",'r')
    data = np.genfromtxt(f,delimiter=None,skip_header=4)
    plt.plot(data[:,2],data[:,4]*1e3,'o')
    plt.xlabel('Frequency (GHz)')
    plt.ylabel('Flux (mJy')
    f.close()
## You can see a quick plot, and you also now have the spectra written
## out to files *.spec.txt
## You can also explore in CARTA or CASA imview

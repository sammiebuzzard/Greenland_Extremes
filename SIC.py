#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 12:46:22 2018

@author: samanthabuzzard

Code to plot and create GIF of sea ice concentration data downloaded from https://daacdata.apps.nsidc.org/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/daily/ using wget (https://nsidc.org/support/faq/what-options-are-available-bulk-downloading-data-https-earthdata-login-enabled)
Adapted from https://github.com/CPOMUCL/Reading_Binary 

"""


import numpy as np
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
from mpl_toolkits.basemap import Basemap, shiftgrid, interp
import scipy.io
from scipy.interpolate import griddata
import datetime
import glob
import imageio

year=1987

#Reading binary data in python: example Sea Ice Concentration data from NSIDC
dimX = 304 #number of rows
dimY = 448 #number of columns
NSIDC_d = '/Volumes/Hackday/daacdata.apps.nsidc.org/pub/DATASETS/nsidc0051_gsfc_nasateam_seaice/final-gsfc/north/daily/'+str(year)+'/'
file_end="_n07_v1.1_n.bin"

files=glob.glob(NSIDC_d+'*')

for file in files:

    time_use = file[len(file)-23:len(file)-15]
    
    infile = NSIDC_d+"nt_"+time_use+file_end
    with open(infile, 'rb') as fr:
        hdr = fr.read(300)
        ice = np.fromfile(fr, dtype=np.uint8)    
    ice = ice.reshape(dimY,dimX)
    ice = np.flipud(ice)
    ice = ice / 250.
    plt.figure(figsize=[10,20])
    mapC = Basemap(projection='npstere', lon_0=-45, boundinglat=50)
    
    img = mapC.imshow(ice, interpolation='none', cmap='YlGnBu')
    
    plt.savefig('/Volumes/Hackday/Figures/'+time_use+'.png')
    print(time_use)
    plt.clf()
    

im_files = glob.glob('/Volumes/Hackday/Figures/*'+str(year)+'*')
images=[]
for filename in im_files:
    images.append(imageio.imread(filename))
imageio.mimsave('/Volumes/Hackday/'+str(year)+'.gif', images)


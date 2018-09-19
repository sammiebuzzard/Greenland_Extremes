# -*- coding: utf-8 -*-
"""
Created on Wed Sep 19 13:49:48 2018

@author: gh415
"""

import matplotlib
import mpl_toolkits
#from mpl_toolkits.basemap import Basemap, shiftgrid
from pylab import *
import numpy.ma as ma
import pandas as pd
import seaborn as sns
#sns.set_style("whitegrid")
# Set folder links
dataPath = '\\\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Data'
figpath='\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Figures'
dataOutPath='\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\DataOutput'

plt.style.available
plt.style.use('ggplot')

import warnings; warnings.simplefilter('ignore')

# Read data into a dataframe. 
#KapMorris201704301099999
# wind is column 10, ignore for now
dF1 = pd.read_csv('\\\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Data\KapMorris201704301099999.csv', header=1, usecols=[1, 13], 
                 names=['timeStamp', 'tempRaw'])
dF1.tail(3) #provides information about the dataframe

dF2 = pd.read_csv('\\\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Data\KapMorris201804301099999.csv', header=1, usecols=[1, 13], 
                 names=['timeStamp', 'tempRaw'])
dF = pd.concat([dF1, dF2])
dF.tail(3)

#dF3 = pd.read_csv('\\\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Data\Kap_Morris_2018.csv', header=1, usecols=[1, 5], 
                 #names=['heading', 'speed'])
dF3 = pd.read_csv('\\\\isad.isadroot.ex.ac.uk\UOE\User\GitHub\extreme-Arctic-events\Data\Kap_Morris_2018.csv', header=1, usecols=[0,4,5], 
                 names=['date','heading', 'speed'])
#formatting wind heading to v
#dF3['V'] = dF3.loc[dF3['speed']]
#wind_heading = dF3[:,0]


# divide raw temp readings by 10
dF['temp'] = pd.Series([int(x[0:5])/10. for x in dF['tempRaw'].values], index=dF.index)
# Extract date/time information.
# Bit crude but works..
dF['year'] = pd.Series([int(x[0:4]) for x in dF['timeStamp'].values], index=dF.index)
dF['month'] = pd.Series([int(x[5:7]) for x in dF['timeStamp'].values], index=dF.index)
dF['day'] = pd.Series([int(x[8:10]) for x in dF['timeStamp'].values], index=dF.index)
dF['hour'] = pd.Series([int(x[11:13]) for x in dF['timeStamp'].values], index=dF.index)

dF.head()

# Filter out the negative (NaN) values

dF.loc[dF['temp'] > 900,'temp'] = np.nan
dF=dF.drop(columns=['tempRaw'])
dF.tail(3)

# Let's take a look at winter 2018 data 

fig = figure(figsize=(9,4))
#dF.loc[(dF['year'] == 2017) & dF['month'].isin([2, 3])]['timeStamp'].values,
ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='r')
#ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([7, 8])]['temp'].values, color='r')
#ax = plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='k')
a = ylabel('Air Temperature (C)')
a = xlabel('Hourly record')
b=suptitle('Winter 2018 air temperatures from Kap Morris')

#July and August 2018 data
fig = figure(figsize=(9,4))
#dF.loc[(dF['year'] == 2017) & dF['month'].isin([2, 3])]['timeStamp'].values,
#ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='r')
#ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([8])]['temp'].values, color='r')
timeaxhr = range(len(dF.loc[(dF['year'] == 2018) & dF['month'].isin([8])]['temp'].values))
myInt = float(24)
timeaxday = [x / myInt for x in timeaxhr]
ax = plt.plot(timeaxday,dF.loc[(dF['year'] == 2018) & dF['month'].isin([8])]['temp'].values, color='r')
#ax = plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='k')
plt.ylim((-3,17.5))
a = ylabel('Air Temperature (C)')
a = xlabel('Hourly record (Days)')
b=suptitle(' August 2018 air temperatures from Kap Morris')

#July 2018 data
fig = figure(figsize=(9,4))
#dF.loc[(dF['year'] == 2017) & dF['month'].isin([2, 3])]['timeStamp'].values,
#ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='r')
#ax = plt.plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([8])]['temp'].values, color='r')
timeaxhr = range(len(dF.loc[(dF['year'] == 2018) & dF['month'].isin([7])]['temp'].values))
myInt = float(24)
timeaxday = [x / myInt for x in timeaxhr]
ax = plt.plot(timeaxday,dF.loc[(dF['year'] == 2018) & dF['month'].isin([7])]['temp'].values, color='r')
#ax = plot(dF.loc[(dF['year'] == 2018) & dF['month'].isin([2, 3])]['temp'].values, color='k')
plt.ylim((-3,17.5))
a = ylabel('Air Temperature (C)')
a = xlabel('Hourly record (Days)')
b=suptitle('July 2018 air temperatures from Kap Morris')
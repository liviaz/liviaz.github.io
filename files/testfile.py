# -*- coding: utf-8 -*-
"""
Analyzing trees in San Francisco

"""

import pandas as pd
import numpy as np
from functions import *


csvFile = 'C:\Users\liviaz\Dropbox\JobSearch\Project\Street_Tree_List.csv';
treeDataRaw = pd.read_csv(csvFile)

# variables to keep:
# treeID, qCaretaker, qSpecies, qAddress, PlantDate, Latitude, Longitude
# check for NaN
dataMissing = (pd.isnull(treeDataRaw.TreeID) | pd.isnull(treeDataRaw.qCaretaker)
            | pd.isnull(treeDataRaw.qSpecies) | pd.isnull(treeDataRaw.qAddress) 
            | pd.isnull(treeDataRaw.PlantDate) | pd.isnull(treeDataRaw.Latitude)
            | pd.isnull(treeDataRaw.Longitude))

treeDataRaw = treeDataRaw[dataMissing == False]
treeDataRaw = treeDataRaw[(['TreeID', 'qCaretaker', 'qSpecies', 'qAddress', 
                      'PlantDate', 'Latitude', 'Longitude'])]



#%%

# parse strings in PlantDate and qSpecies
speciesSplit = treeDataRaw['qSpecies'].str.split(' :: ')
dateSplit = treeDataRaw['PlantDate'].str.split(' ')

speciesLatin = pd.Series(np.empty(speciesSplit.shape, object), \
    index=treeDataRaw.index, name='speciesL')
speciesCommon = pd.Series(np.empty(speciesSplit.shape, object), \
    index=treeDataRaw.index, name='speciesC')
plantYear = pd.Series(np.empty(dateSplit.shape, object), \
    index=treeDataRaw.index, name='plantYear')
invalidIndex = pd.Series(np.empty(len(plantYear), bool), index=treeDataRaw.index)

for index in speciesSplit.index:
    
    invalidIndex[index] = False    
    currSpecies = speciesSplit[index]
    currDateSplit = dateSplit[index][0].split('/')
    
    if len(currSpecies) < 2:
        speciesLatin[index] = None
        speciesCommon[index] = None
        invalidIndex[index] = True
    else:
        speciesLatin[index] = currSpecies[0]
        speciesCommon[index] = currSpecies[1]


    if len(currDateSplit) < 3:
        plantYear[index] = None
        invalidIndex[index] = True
    else:
        plantYear[index] = int(currDateSplit[2])
        
        

#%% 
# recombine everything into one data frame
treeDataProc = treeDataRaw[['qCaretaker', 'Latitude', 'Longitude']]
treeDataProc = treeDataProc.join([speciesLatin, speciesCommon, plantYear])
treeDataProc = treeDataProc[invalidIndex == False]




#%% Now start plotting ...

from gmplot import *

gmap = gmplot.GoogleMapPlotter(37.758938386239002, -122.48853172315201, 16)

gmap.scatter(treeDataProc.loc[:,'Latitude'], treeDataProc.loc[:,'Longitude'],  '#0000AA', size=20, marker=False)
#gmap.heatmap(treeDataProc.loc[:,'Latitude'], treeDataProc.loc[:,'Longitude'])

gmap.draw("mymap.html")










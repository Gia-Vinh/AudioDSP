
import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import utilFunctions as UF
import harmonicModel as HM
import stft

eps = np.finfo(float).eps

inputFile='../../sounds/cello-phrase.wav'
stdThsld = 10
minNoteDur = 0.1
winStable = 3
window = 'hamming'
M = 1025
N = 2048
H = 256
f0et = 5.0
t = -100
minf0 = 310
maxf0 = 650



fs, x = UF.wavread(inputFile)                               #reading inputFile
w  = get_window(window, M)                                  #obtaining analysis window    
f0 = HM.f0Detection(x, fs, w, N, H, t, minf0, maxf0, f0et)  #estimating F0

### your code here

# 1. convert f0 values from Hz to Cents (as described in pdf document)
f0[np.where(f0<eps)] = eps
f0Cent = 1200 * np.log2(f0 / 55.0)

#2. create an array containing standard deviation of last winStable samples
devf0 = np.zeros(f0Cent.size)
for i in range(winStable, f0Cent.size):
	devf0[i] = np.std(f0Cent[i-winStable:i])
    

stablePts = np.where(devf0<stdThsld)[0]

#4. create segments of continuous stable points such that consecutive stable points belong to same segment
segmentsList = np.array([[]], dtype = int).reshape(0,2)          #list of stable segment
isConsecutive = False                       #create a flag to check consecutivity between stable node
stbSegment_start = 0                        #initialize start and end indexes for stable segment
stbSegment_end = 0
    
for i in range(0,stablePts.size-1):            #iterate through stablePtsId until 2nd last element, look for consecutive point
	if (isConsecutive == False):                    #if not already in consecutive stable region, check for it
		if (stablePts[i+1] - stablePts[i] == 1):          #if true, this is the start of a new consecutive stable region
			stbSegment_start == stablePts[i]                 #update segment starting point
			isConsecutive = True
			continue
		else:                                                    #if false,still in a non - consecutive region
			continue
        
	else: #isConsecutive == True                #already in a consecutive stable region, check for the end
		if (stablePts[i+1] - stablePts[i] == 1):          #if true, we are still in the same consecutive stable region
			continue
		else:                                                 #if false, reached the end of the the consecutive stable region
			stbSegment_end = stablePts[i]   #update segment ending point
			isConsecutive = False
                #append the starting and ending point of the segment to the segment list
			segmentsList = np.vstack([segmentsList, np.array([[stbSegment_start, stbSegment_end]])])
    
if (isConsecutive == True): #that means the final stale region runs until the end of stablePtsId
	segmentsList = np.vstack([segmentsList, np.array([[stbSegment_start, stablePtsId[-1] ]])])



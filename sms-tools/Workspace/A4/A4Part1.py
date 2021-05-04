import numpy as np
from scipy.signal import get_window
from scipy.fftpack import fft, fftshift
import math
import matplotlib.pyplot as plt
eps = np.finfo(float).eps

""" 
A4-Part-1: Extracting the main lobe of the spectrum of a window

Write a function that extracts the main lobe of the magnitude spectrum of a window given a window 
type and its length (M). The function should return the samples corresponding to the main lobe in 
decibels (dB).

To compute the spectrum, take the FFT size (N) to be 8 times the window length (N = 8*M) (For this 
part, N need not be a power of 2). 

The input arguments to the function are the window type (window) and the length of the window (M). 
The function should return a numpy array containing the samples corresponding to the main lobe of 
the window. 

In the returned numpy array you should include the samples corresponding to both the local minimas
across the main lobe. 

The possible window types that you can expect as input are rectangular ('boxcar'), 'hamming' or
'blackmanharris'.

NOTE: You can approach this question in two ways: 1) You can write code to find the indices of the 
local minimas across the main lobe. 2) You can manually note down the indices of these local minimas 
by plotting and a visual inspection of the spectrum of the window. If done manually, the indices 
have to be obtained for each possible window types separately (as they differ across different 
window types).

Tip: log10(0) is not well defined, so its a common practice to add a small value such as eps = 1e-16 
to the magnitude spectrum before computing it in dB. This is optional and will not affect your answers. 
If you find it difficult to concatenate the two halves of the main lobe, you can first center the 
spectrum using fftshift() and then compute the indexes of the minimas around the main lobe.


Test case 1: If you run your code using window = 'blackmanharris' and M = 100, the output numpy 
array should contain 65 samples.

Test case 2: If you run your code using window = 'boxcar' and M = 120, the output numpy array 
should contain 17 samples.

Test case 3: If you run your code using window = 'hamming' and M = 256, the output numpy array 
should contain 33 samples.

"""
def extractMainLobe(window, M):
    """
    Input:
            window (string): Window type to be used (Either rectangular ('boxcar'), 'hamming' or '
                blackmanharris')
            M (integer): length of the window to be used
    Output:
            The function should return a numpy array containing the main lobe of the magnitude 
            spectrum of the window in decibels (dB).
    """

    w = get_window(window, M)                   # get the window
    
    ### Your code here
    N = 8*M                                                 #get fft size
    
    #Construct the FFT buffer
    fftbuffer = np.zeros(N)
    fftbuffer[:M] = w[:M]
    
    #Apply FFT and shift the zero freq. component to the middle of the array
    W = fft(fftbuffer)
    W = fftshift(W)
    #Get the magnitude spectrume
    mW = abs(W)
    mW = mW + eps                                   #add small offset to prevent log10(0) case
    mW = 20 * np.log10(mW)                      #Convert to dB scale
    
    """Since the main lobe is always in the middle, it is safe to jump into the middle of the spectrum
    then start to find the local minima. In addition, our window is a real funciton, so the spectrum is symmetry.
    => only search the local minimum in the positive (+) direction
    """
    MLP = N/2                                       #MLP = main lobe peak
    localMinIndex = 1                             #Initialize the localMinIndex to be next to MLP, the correct localMIn 
                                                           #will be the one smaler than its two neighbors
    while (mW[MLP+ localMinIndex]<= mW[MLP+localMinIndex-1])  \
    and  \
    (mW[MLP+ localMinIndex] >= mW[MLP+localMinIndex+1]):
        localMinIndex += 1
        
    #return the whole mainLobe
    mainLobe = mW[MLP-localMinIndex:MLP+localMinIndex+1]
    
    return mainLobe
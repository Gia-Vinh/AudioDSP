##Create sin wave to test A3Part1
import numpy as np

def sumOf2Sine(a1, a2, f1, f2, fs):
    t = np.arange(0, 5, 1.0/fs)
    x1 = a1 * np.cos(2 * np.pi * f1 * t)
    x2 = a2 * np.cos(2 * np.pi * f2 * t)
    x = x1+ x2
    return x

def fixLengthSine(f, M, fs):
    nv = np.arange(0, M)
    tv = nv/float(fs)
    x = np.cos(2*np.pi*f*tv)
    return x    
    
def sumOf4Sine(f1, f2, f3, f4, fs):
    t = np.arange(0,5,1.0/fs)
    x1= sumOf2Sine(1, 1, f1, f2, fs)
    x2 = sumOf2Sine(1, 1, f3, f4, fs)
    return x1+x2    
    
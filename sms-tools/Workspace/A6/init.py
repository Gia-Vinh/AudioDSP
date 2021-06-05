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

inputFile='../../sounds/piano.wav'
t1 = 0.2
t2 = 0.4
window = 'hamming'
M = 2047
N = 2048
H = 128
f0et = 5.0
t = -90
minf0  = 130
maxf0 = 180
nH = 25

inputFile = '../../sounds/piano.wav'
window = 'blackman'
M = 513
N = 1024
H = 128


import os
import sys
import numpy as np
import math
from scipy.signal import get_window
import matplotlib.pyplot as plt

sys.path.append(os.path.join(os.path.dirname(os.path.realpath(__file__)), '../../software/models/'))
import stft
import utilFunctions as UF
eps = np.finfo(float).eps

(fs, x) = UF.wavread(inputFile)

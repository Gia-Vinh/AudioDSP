import numpy as np
from scipy.signal import triang
from scipy.fftpack import fft

x = triang(15)
fftbuffer = np.zeros(15)
fftbuffer[:8] = x[7:]
fftbuffer[8:] = x[:7]
X = fft(x)
mX = abs(X)
pX = np.angle(x)


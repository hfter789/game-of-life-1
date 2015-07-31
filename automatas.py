import numpy as np
from lib import fft_convolve2d

def conway(state, k=None):
	"""
	Conway's game of life state transition
	"""

	# set up kernel if not given
	if k == None:
		m, n = state.shape
		k = np.zeros((m, n))
		k[m/2-1 : m/2+2, n/2-1 : n/2+2] = np.array([[1,1,1],[1,0,1],[1,1,1]])

	# computes sums around each pixel
	b = fft_convolve2d(state,k).round()
	c = np.zeros(b.shape)

	c[np.where((b == 2) & (state == 1))] = 1
	c[np.where(b == 3)] = 1
	# return new state
	return c
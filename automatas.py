import numpy as np
from lib import fft_convolve2d

def transitionHelper(state, k=None):
	# set up kernel if not given
	if k == None:
		m, n = state.shape
		k = np.zeros((m, n))
		k[m/2-1 : m/2+2, n/2-1 : n/2+2] = np.array([[1,1,1],[1,0,1],[1,1,1]])

	# computes sums around each pixel
	b = fft_convolve2d(state,k).round()
	c = np.zeros(b.shape)

	return b,c

def conway(state, k=None):
	"""
	Conway's game of life state transition
	"""

	b,c = transitionHelper(state,k)

	c[np.where((b == 2) & (state == 1))] = 1
	c[np.where(b == 3)] = 1
	# return new state
	return c

def day_and_night(state, k=None):
	"""
	'Day & night' automata state transition
	http://www.conwaylife.com/wiki/Day_%26_Night
	"""
	b,c = transitionHelper(state,k)

	c[np.where((b == 3) & (state == 1))] = 1
	c[np.where((b == 6) & (state == 1))] = 1
	c[np.where((b == 7) & (state == 1))] = 1
	c[np.where((b == 8) & (state == 1))] = 1

	c[np.where((b == 3) & (state == 0))] = 1
	c[np.where((b == 4) & (state == 0))] = 1
	c[np.where((b == 6) & (state == 0))] = 1
	c[np.where((b == 7) & (state == 0))] = 1
	c[np.where((b == 8) & (state == 0))] = 1

	# return new state
	return c


def high_life(state, k=None):
	"""
	'HighLife' automata state transition
	http://www.conwaylife.com/wiki/HighLife
	"""
	b,c = transitionHelper(state,k)

	c[np.where((b == 2) & (state == 1))] = 1
	c[np.where((b == 3) & (state == 1))] = 1

	c[np.where((b == 3) & (state == 0))] = 1
	c[np.where((b == 6) & (state == 0))] = 1

	# return new state
	return c

def replicator(state, k=None):
	"""
	'Replicator' cellular automaton state transition
	http://www.conwaylife.com/wiki/Replicator_(CA)
	"""
	b,c = transitionHelper(state,k)
	# checks the values, and sets alive vs. dead state
	c[np.where((b + 1) % 2 == 0)] = 1

	# return new state
	return c

def seeds(state, k):
	"""
	'Seeds' cellular automaton state transition
	http://www.conwaylife.com/wiki/Seeds
	"""
	b,c = transitionHelper(state,k)
	# checks the values, and sets alive vs. dead state
	c[np.where((b == 2) & (state == 0))] = 1

	# return new state
	return c

def two_by_two(state, k=None):
	"""
	'2x2' automata state transition
	http://www.conwaylife.com/wiki/2x2
	"""
	b,c = transitionHelper(state,k)
	# checks the values, and sets alive vs. dead state

	c[np.where((b == 1) & (state == 1))] = 1
	c[np.where((b == 2) & (state == 1))] = 1
	c[np.where((b == 5) & (state == 1))] = 1

	c[np.where((b == 3) & (state == 0))] = 1
	c[np.where((b == 6) & (state == 0))] = 1

	# return new state
	return c
import sched, time
import numpy as np
import time
from lib import fft_convolve2d
import matplotlib.pyplot as plt
import matplotlib as mpl

mpl.rcParams['toolbar'] = 'None'
# set up board
plt.ion()
m,n = 30,30
UPDATE_INTERVAL = 0.01
A = np.random.random(m*n).reshape((m, n)).round()
fig = plt.figure()
fig.canvas.set_window_title('Game of Life')
img_plot = plt.imshow(A, interpolation="nearest", cmap = plt.cm.gray)
plt.axis('off')
plt.subplots_adjust(left=0, right=1, top=1, bottom=0)
plt.show(block=False)
global x
global y
x = y = -1

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

def onclick(event):
	global x
	global y
	x = int(event.xdata)
	y = int(event.ydata)

if __name__ == "__main__":
	# plot each frame
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	while True:
		A = conway(A)
		if x != -1:
			A[y][x] = 1
			x = -1
			y = -1
		img_plot.set_data(A)
		plt.draw()
		plt.pause(UPDATE_INTERVAL)

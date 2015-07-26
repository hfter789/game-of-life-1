import sched, time
import numpy as np
import time
from lib import fft_convolve2d
import matplotlib.pyplot as plt
plt.ion()

UPDATE_INTERVAL = 0.01

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
	print 'button=%d, x=%d, y=%d, xdata=%f, ydata=%f'%(
		event.button, event.x, event.y, event.xdata, event.ydata)

def updatePlot(sc, img_plot, A):
	A = conway(A)
	img_plot.set_data(A)
	plt.draw()
	#update_interval in sec
	sc.enter(UPDATE_INTERVAL, 1, updatePlot, (sc,img_plot,A,))
	
if __name__ == "__main__":
	# set up board
	m,n = 100,100
	A = np.random.random(m*n).reshape((m, n)).round()

	# plot each frame
	fig = plt.figure()
	cid = fig.canvas.mpl_connect('button_press_event', onclick)
	img_plot = plt.imshow(A, interpolation="nearest", cmap = plt.cm.gray)
	s = sched.scheduler(time.time, time.sleep)
	# plt.show(block=False)
	s.enter(UPDATE_INTERVAL, 1, updatePlot, (s,img_plot,A,))
	s.run()


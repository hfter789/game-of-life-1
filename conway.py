import sched, time
import numpy as np
import time
from lib import fft_convolve2d
import matplotlib.pyplot as plt
import matplotlib as mpl
from matplotlib.widgets import Button

#remove the default toolbar from figure
# mpl.rcParams['toolbar'] = 'None'

# set up board
m,n = 30,30
UPDATE_INTERVAL = 0.01
update = False

plt.ion()
A = np.random.random(m*n).reshape((m, n)).round()
# A = np.zeros((m,n)).round()
fig = plt.figure()
fig.canvas.set_window_title('Game of Life')
img_plot = plt.imshow(A, interpolation="nearest", cmap = plt.cm.gray)

#remove the axis
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


def startUpdate(event):
	global update
	update = True
	print 'start'

def pauseUpdate(event):
	global update
	update = False

def stopUpdate(event):
	global update
	global A
	global img_plot
	update = False
	A = np.zeros((m,n)).round()
	img_plot.set_data(A)
	plt.draw()
	print 'stop'

def mouseclick(event):
	global x
	global y
	global A
	global img_plot
	# require a right click
	if event.button != 3:
		return
	x = int(event.xdata)
	y = int(event.ydata)
	print y,x

if __name__ == "__main__":
	cid = fig.canvas.mpl_connect('button_press_event', mouseclick)

	#start button
	axstart = plt.axes([0.89, 0.05, 0.1, 0.075])
	bstart = Button(axstart, 'Start')
	bstart.on_clicked(startUpdate)

	#pause button
	axpause = plt.axes([0.89, 0.15, 0.1, 0.075])
	bpause = Button(axpause, 'Pause')
	bpause.on_clicked(pauseUpdate)

	#stop button
	axstop = plt.axes([0.89, 0.25, 0.1, 0.075])
	bstop = Button(axstop, 'Stop')
	bstop.on_clicked(stopUpdate)
	plt.draw()

	while True:
		if x != -1:
			print 'in1',A[y][x]
			A[y][x] = 1
			x = -1
			y = -1
			img_plot.set_data(A)
			plt.draw()
		if update:
			print 'in2'
			A = conway(A)
			img_plot.set_data(A)
			plt.draw()
		plt.pause(UPDATE_INTERVAL)

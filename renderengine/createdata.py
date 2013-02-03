from matplotlib.pyplot import *
import numpy as np
from matplotlib import *
import matplotlib.cm as cm
from matplotlib.backends.backend_agg import FigureCanvasAgg 
from matplotlib.figure import Figure
from scipy.ndimage.filters import *
import time
import pdb
import matplotlib.pyplot as plt
import numpy as np
import numpy.random as npr
from random import choice
import time


class Renderer:

	def __init__(self):
		self.size_x = 3
		self.size_y = 3
		self.size_x, self.size_y = 300,300
		my_dpi = 100
		inches_sizex, inches_sizey = self.size_x/my_dpi, self.size_y/my_dpi
		self.f = Figure(frameon=False, dpi=my_dpi)
	    	self.f.set_size_inches(inches_sizex, inches_sizey)
	    	self.ax = Axes(self.f, [0., 0., 1., 1.])
	    	self.ax.set_axis_off()
	    	self.f.add_axes(self.ax)
		self.canvas = FigureCanvasAgg(self.f)


	def render_thing(self,state,thing):
	    self.ax.text(float(thing['left'])/state['params']['room_self.size_x'], float(thing['top'])/state['params']['room_self.size_y'], thing['id'], size = thing['size'])
	    self.canvas.draw()
	    im_str = self.canvas.tostring_rgb()

	    a = np.fromstring(im_str, dtype=np.uint8)
	    im = a.reshape(self.size_x, self.size_y, 3)

	    im = np.sum(im, 2)
	    im = np.float64(im)
	    im = im/np.max(im)
	    im = 1-im
	    if state['blur']:
	    	bim = gaussian_filter(im, thing['blur_sigsq'], mode='wrap')
	    return bim

	def get_rendered_image(self,state,things):
		for i in range(len(things)):
			bim = self.render_thing(state,things[i])			
			bim = npr.binomial(1, bim/np.max(bim))
			if i == 0:
				bim[bim.nonzero()] = 1
				im = bim
			else:
	    			im[bim.nonzero()] = 1
		return im


	def test(self):
		state = dict()
		state['params'] = {'room_self.size_x':300, 'room_self.size_y':300}
		state['blur'] = True

		things = []
		things.append({'id':'A', 'size':50, 'left':100, 'top':100,'blur_sigsq':50})
		things.append({'id':'Z', 'size':20, 'left':0, 'top':100,'blur_sigsq':10})
		things.append({'id':'C', 'size':30, 'left':40, 'top':120,'blur_sigsq':0})
		things.append({'id':'E', 'size':50, 'left':140, 'top':160,'blur_sigsq':3})
		things.append({'id':'M', 'size':20, 'left':240, 'top':20,'blur_sigsq':0})
	
		t0 = time.time()
		im = self.get_rendered_image(state,things)
		t1 = time.time()
		print t1-t0

		imshow(im, cmap=cm.Greys)
		show()

r = Renderer()
r.test()

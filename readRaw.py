import os
import csv
import time

import plotly.plotly as py
import plotly.graph_objs as go

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib import interactive
interactive(True)

# Scientific libraries
from numpy import arange,array,ones
from scipy import stats


rootdir = '/Users/Mus/Desktop/070917/'

for subdir, dirs, files in os.walk(rootdir):
	for file in files:
		fSplit = file.split(".")
		fName = fSplit[0]
		fExt = fSplit[1]
		if (fExt == 'txt'):
			fName = fName.split("_")
			if(len(fName)>3):
				if(fName[3] == 'IV'):	
					fDir = os.path.join(subdir, file)
					dIV =[]
					x = []
					y = []
					with open(fDir,'r') as f:
						next(f) # skip headings
						reader=csv.reader(f,delimiter='\t')
						dIV = list(reader)
					dIV.pop(0)
					dIV.pop(1)
					
					x = array([float(row[1]) for row in dIV])
					y = array([float(row[0]) for row in dIV])

					xIndex = round(x.size/2)
					yIndex = round(y.size/2)

					slope, intercept, r_value, p_value, std_err = stats.linregress(x[xIndex-2:xIndex+2],y[xIndex-2:xIndex+2])
					line = slope * x + intercept
					
					plt.plot(x,y,'o', x, line)
					pylab.title('Linear Fit with Matplotlib')
					ax = plt.gca()
					ax.set_axis_bgcolor((0.898, 0.898, 0.898))
					fig = plt.gcf()
					
					plt.savefig(fDir+'_'+str(time.time())+'.png')
					
					plt.close()	
#fDir = '/Users/Mus/Desktop/070917/070917_1_0_IV.txt'#input("What is the full file path? ")
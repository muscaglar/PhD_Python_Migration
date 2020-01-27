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

rootdir = '/Users/Mus/Downloads/101117/1MKNO3_1'

for root, dirs, files in os.walk(rootdir):
	for file_ in files:
		print('file', os.path.join(root, file_))

with open(file_,'rb') as tsvin, open('new.csv', 'wb') as csvout:
	tsvin = csv.reader(tsvin, delimiter='\t')
	csvout = csv.writer(csvout)

	for row in tsvin:
		count = int(row[4])
		if count > 0:
			csvout.writerows([row[2:4] for _ in xrange(count)])
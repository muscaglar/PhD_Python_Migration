import pyodbc #SQL connection
from azure.storage.blob import BlockBlobService

import os
import csv

# MatPlotlib
import matplotlib.pyplot as plt
from matplotlib import pylab
from matplotlib import interactive
interactive(True)

import numpy as np
from scipy import stats

#Blobs
mKey = 'KEY'
mName = 'michaelwalkerphd'

#Server
server = 'tcp:michael-walker.database.windows.net'
database = 'ExperimentsDB'
username = 'mcaglar'
password = 'PASSWORD'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#passing in cID

cID = input("Which capillary should I analyse? ")

eID = []
eDate = []
eNo = []

for row in cursor.execute("SELECT * FROM Experiments WHERE Capillary = ? AND Suppressed != 4", cID):
	eID.append(row[0])
	eDate.append(row[1])
	eNo.append(row[2])
#row will contain: 0.  id	1.  Date	2.  No	3.  Capillary	4.  CapPh	5.  ResPh	6.  Voffset	7.  Ioffset	8.  Resistance	9.  LowRes	10.  HighRes	11.  nPerm	12.  pPerm	13.  PermOffset	14.  AnalysisDate	15.  CapillarySln	16.  CapillaryConc	17.  ReservoirSln	18.  ReservoirConc	19.  Sealed	20.  Suppressed	21.  FileType	22.  Comment

#Get Cloud Data
class fileDetails:
	def __init__(self, date, number, extension):
		self.date = date
		self.number = number
		self.extension = extension
		self.fileName = str(date[8:10]) + str(date[5:7])  + str(date[2:4]) + '_'+ str(number) + '.' + extension #ddmmyy_no.txt

date = eDate[0]
number = eNo[0]

#LoadFile
fDetails = fileDetails(date, number, "txt")
bContainer = "data"
cName = str(fDetails.fileName)
fDir = str('cache/' + cName)
#GetFile
#DownloadBlobFromContainer
if not os.path.exists('cache'):
	os.makedirs('cache')

block_blob_service = BlockBlobService(account_name = mName, account_key=mKey)

if os.path.isfile(fDir):
	print('File exists')
else:
	block_blob_service.get_blob_to_path(bContainer, cName, fDir)

dIV =[]

with open(fDir,'r') as f:
	next(f) # skip headings
	reader=csv.reader(f,delimiter='\t')
	dIV = list(reader)

dIV.pop(0)

x = np.array([float(row[1]) for row in dIV])
y = np.array([float(row[0]) for row in dIV])

xIndex = round(x.size/2)
yIndex = round(y.size/2)

slope, intercept, r_value, p_value, std_err = stats.linregress(x[xIndex-2:xIndex+2],y[xIndex-2:xIndex+2])
line = slope * x + intercept

plt.plot(x,y,'o', x, line)
pylab.title('Linear Fit with Matplotlib')
ax = plt.gca()
#ax.set_axis_bgcolor((0.898, 0.898, 0.898))
fig = plt.gcf()

plt.savefig(fDir+'.png')

#Got one IV file. Now to IVAnalyse. 

#Does not check if it is attempting to plot a valid IV file as opposed to spectra, trace etc

	
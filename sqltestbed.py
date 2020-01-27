#!/usr/bin/python

import pyodbc
import DBSupportLib
import datetime
import dateutil.parser as parser
from azure.storage.blob import BlockBlobService
import os
import csv

import matplotlib.pyplot as plt
from matplotlib import interactive
interactive(True)

server = 'tcp:michael-walker.database.windows.net'
database = 'ExperimentsDB'
username = 'mcaglar'
password = 'PASSWORD'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Date = (str(17+2000)+"-"+'08'+ "-" + str(20))
#AnalysisDate = Date

#storageexplorer://v=1&accountid=%2Fsubscriptions%2F7616c442-cf6d-46d1-a355-7d5e243da7ae%2FresourceGroups%2Fmichael-walker%2Fproviders%2FMicrosoft.Storage%2FstorageAccounts%2Fmichaelwalkerphd&subscriptionid=7616c442-cf6d-46d1-a355-7d5e243da7ae

mKey = 'KEY'
mName = 'michaelwalkerphd'

block_blob_service = BlockBlobService(account_name = mName, account_key=mKey)

if not os.path.exists('cache'):
	os.makedirs('cache')
	
block_blob_service.get_blob_to_path('data', '140916_12.txt', 'cache/140916_12.txt')

dIV =[]

with open('cache/140916_12.txt','r') as f:
	next(f) # skip headings
	reader=csv.reader(f,delimiter='\t')
	dIV = list(reader)

dIV.pop(0)

x = [float(row[1]) for row in dIV]
y = [float(row[0]) for row in dIV]

print(x)
print(y)

plt.plot(x, y)
plt.savefig(fDir+'.png')



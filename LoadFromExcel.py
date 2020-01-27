import xlrd #Parse Excel
import pymysql #SQL connection
import pyodbc #SQL connection
import datetime #Date time formats
import DBSupportLib #Only using this for the date time -> Could probably code it out

def readSpreadsheetRow(data, sRow, sCol):
	iRow = data.row_values(sRow)
	for dRow in range(0,sCol):
		del iRow[dRow] 
	iRow = [x for x in iRow if x] #This removes all empty entries from the list. Lookup List Comprehensions - I don't understand this fully
	return iRow

def readSpreadsheetMatrix(data, sRow, sCol, nRows, nCols):
	_matrix=[]
	_row=[]
	for col in range (sCol, sCol + nCols):
		iCol = data.col_values(col)
		for dRow in range(0,sRow):
			del iCol[0]
		iCol = [x for x in iCol if x]
		_row.append(iCol)
	_matrix.append(_row)
	return _matrix

nInvestigator = input("What is your investigator number? ")
#nInvestigator = 5
#pName = input("What is the name of the Excel File? ")
pName = "/Users/Mus/Downloads/ExperimentSummaries.xlsm"
wName = input("What is the name of the worksheet? ")
#wName = "20082017_python_test"
workbook = xlrd.open_workbook(pName, on_demand = True)
worksheet = workbook.sheet_by_name(wName)

server = 'tcp:michael-walker.database.windows.net'
database = 'ExperimentsDB'
username = 'mcaglar'
password = 'dkIr74BnDwQjdpcc'
driver= '{ODBC Driver 13 for SQL Server}'
cnxn = pyodbc.connect('DRIVER='+driver+';PORT=1433;SERVER='+server+';PORT=1443;DATABASE='+database+';UID='+username+';PWD='+ password)
cursor = cnxn.cursor()

#Date Massaging:
#The date is being formatted such that the 9th of november 2016 is: 091116 as a STRING
#Do not know if this is correct yet

day = int(worksheet.cell(1, 1).value)
month = int(worksheet.cell(1,2).value)
year = int(worksheet.cell(1,3).value)
#if (day < 10):
#	day = (str(0) + str(day))
#if (month < 10):
#	month = (str(0) + str(month))
if (year < 100):
	year = year + 2000
	
dt = datetime.datetime(year, month, day, 0, 0, 0)
date = DBSupportLib.DBDateTime(str(dt))
Date = str(date)


ExptType = worksheet.cell(1,7).value
CapNo = worksheet.cell(3,1).value
CapType = worksheet.cell(4,1).value
CapSol = worksheet.cell(5,1).value
CapConc = worksheet.cell(6,1).value
CapPh = worksheet.cell(7,1).value
MembraneID = worksheet.cell(8,1).value
BareIVCurves = readSpreadsheetRow(worksheet,10,1)
SealedIVCurves = readSpreadsheetRow(worksheet,11,1)
AwayIVCurves = readSpreadsheetRow(worksheet,12,1)
SelectiveIV = readSpreadsheetMatrix( worksheet , 17, 0, 0, 7)
Traces = readSpreadsheetMatrix( worksheet , 17, 11, 0, 9)
CapID = 0

#Now on line 52 of LoadExpFromExcelSummary

for row in cursor.execute("SELECT * FROM Membranes WHERE id LIKE ?", MembraneID):
#	print(row.Name)
#	print(row.Material)
	mID = row.id
	print(row.DateStarted)
	print(row.Details)
	print(row)

#Add Capillaries
cursor.execute("INSERT INTO Capillaries (Date , Type , CapNo , ExptType , investigator) VALUES ( ? ,  ? ,  ? ,  ? ,  ?  )", Date, CapType, CapNo, ExptType, nInvestigator)
cursor.commit()

#Get Capillary ID
for row in cursor.execute("SELECT * FROM Capillaries WHERE Date LIKE ? AND CapNo = ?", Date, CapNo):
	CapID = row.id

Capillary = CapID
CapPh = CapPh
ResPh = CapPh
Voffset = False
Ioffset = False
Resistance = False
LowRes = False
HighRes = False
nPerm = False
pPerm = False
PermOffset = False
AnalysisDate = 'null'
CapillarySln = CapSol
CapillaryConc = CapConc
ReservoirSln = CapSol
ReservoirConc = CapConc
FileType = None
Comment = None


#Add Experiments

for bareIV in BareIVCurves:
	Sealed = 0
	No = bareIV
	Suppressed = 0
	cursor.execute("INSERT INTO Experiments (Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )", Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment)
	cursor.commit()
	
for sealedIV in SealedIVCurves:
	Sealed = mID
	No = sealedIV
	Suppressed = 20
	cursor.execute("INSERT INTO Experiments (Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )", Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment)	
	cursor.commit()
	
for awayIV in AwayIVCurves:
	Sealed = mID
	No = sealedIV
	Suppressed = 21
	cursor.execute("INSERT INTO Experiments (Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )", Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment)		
	cursor.commit()
	
i = 0

print(SelectiveIV)

for sIV in SelectiveIV[0][0]:
	No = sIV
	Sealed = mID
	ReservoirSln = SelectiveIV[0][1][i]
	ReservoirConc = SelectiveIV[0][2][i]
	if not SelectiveIV[0][3]:
		ResPh = 0
	else:
		try:
			ResPh = SelectiveIV[0][3][i]
		except IndexError:
			ResPh = 0
	if not SelectiveIV[0][4]:
		Comment = str(0)
	else:
		try:
			Comment = str(SelectiveIV[0][4][i])
		except IndexError:
			Comment = str(0)
	if not SelectiveIV[0][5]:
		Suppressed = 0
	else:
		try:
			Suppressed = SelectiveIV[0][5][i]
		except IndexError:
			Suppressed = 0
	if not SelectiveIV[0][6]:
		FileType = 0
	else:
		try:
			FileType = SelectiveIV[0][6][i]
		except IndexError:
			FileType = 0
	i = i + 1
	cursor.execute("INSERT INTO Experiments (Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )", Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment)	
	cursor.commit()
	
#Implment AddTraces ie line 45 of AddCapillaries.m
	
eSolution = worksheet.cell(14,6).value
eConc = worksheet.cell(14,8).value
Name = 'ElectrodeSolution'
Value = eConc
StringValue = eSolution

cursor.execute("SELECT * FROM AnalysisValues WHERE Name LIKE ? AND nvCapillary = ?", Name, CapID)
cursor.execute("UPDATE AnalysisValues SET Name =  ? , Value =  ? , StringValue =  ?  WHERE  id = ?", Name, Value, StringValue, CapID)
cursor.commit()

#d = DBSupportCode.DBDateTime;
#d.now();
#NV.setUpdateDate(d);

#All of LoadExpFromExcelSummary has been ported over. However, although capillary entries are made, Experiments and traces are not being added. Perhaps I need to close and re-open the server cursor each time?

cursor.close()
cnxn.close()

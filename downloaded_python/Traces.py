#  Interface for Traces code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Traces: #/*extends TableInterfaceBase*/
    TableName = "Traces";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Date = False;
        self._isChanged_No = False;
        self._isChanged_tCapillary = False;
        self._isChanged_CapPh = False;
        self._isChanged_ResPh = False;
        self._isChanged_CapillarySln = False;
        self._isChanged_CapillaryConc = False;
        self._isChanged_ReservoirSln = False;
        self._isChanged_ReservoirConc = False;
        self._isChanged_tSealed = False;
        self._isChanged_tSuppressed = False;
        self._isChanged_SampleFreq = False;
        self._isChanged_FilterFreq = False;
        self._isChanged_TranslocationsYN = False;
        self._isChanged_Description = False;
    #Access Methods to set and Read Fields --------------
    def setid(self, id):
        self._id = id;
        self._isChanged_id = True;
    def getid(self):
        return (self._id)
    
    def setDate(self, Date):
        self._Date = Date;
        self._isChanged_Date = True;
    def getDate(self):
        return (self._Date)
    
    def setNo(self, No):
        self._No = No;
        self._isChanged_No = True;
    def getNo(self):
        return (self._No)
    
    def settCapillary(self, tCapillary):
        self._tCapillary = tCapillary;
        self._isChanged_tCapillary = True;
    def gettCapillary(self):
        return (self._tCapillary)
    
    def setCapPh(self, CapPh):
        self._CapPh = CapPh;
        self._isChanged_CapPh = True;
    def getCapPh(self):
        return (self._CapPh)
    
    def setResPh(self, ResPh):
        self._ResPh = ResPh;
        self._isChanged_ResPh = True;
    def getResPh(self):
        return (self._ResPh)
    
    def setCapillarySln(self, CapillarySln):
        self._CapillarySln = CapillarySln;
        self._isChanged_CapillarySln = True;
    def getCapillarySln(self):
        return (self._CapillarySln)
    
    def setCapillaryConc(self, CapillaryConc):
        self._CapillaryConc = CapillaryConc;
        self._isChanged_CapillaryConc = True;
    def getCapillaryConc(self):
        return (self._CapillaryConc)
    
    def setReservoirSln(self, ReservoirSln):
        self._ReservoirSln = ReservoirSln;
        self._isChanged_ReservoirSln = True;
    def getReservoirSln(self):
        return (self._ReservoirSln)
    
    def setReservoirConc(self, ReservoirConc):
        self._ReservoirConc = ReservoirConc;
        self._isChanged_ReservoirConc = True;
    def getReservoirConc(self):
        return (self._ReservoirConc)
    
    def settSealed(self, tSealed):
        self._tSealed = tSealed;
        self._isChanged_tSealed = True;
    def gettSealed(self):
        return (self._tSealed)
    
    def settSuppressed(self, tSuppressed):
        self._tSuppressed = tSuppressed;
        self._isChanged_tSuppressed = True;
    def gettSuppressed(self):
        return (self._tSuppressed)
    
    def setSampleFreq(self, SampleFreq):
        self._SampleFreq = SampleFreq;
        self._isChanged_SampleFreq = True;
    def getSampleFreq(self):
        return (self._SampleFreq)
    
    def setFilterFreq(self, FilterFreq):
        self._FilterFreq = FilterFreq;
        self._isChanged_FilterFreq = True;
    def getFilterFreq(self):
        return (self._FilterFreq)
    
    def setTranslocationsYN(self, TranslocationsYN):
        self._TranslocationsYN = TranslocationsYN;
        self._isChanged_TranslocationsYN = True;
    def getTranslocationsYN(self):
        return (self._TranslocationsYN)
    
    def setDescription(self, Description):
        self._Description = Description;
        self._isChanged_Description = True;
    def getDescription(self):
        return (self._Description)
    
    def Initialise(self):
        self.setid(0);
        self.setDate( DBDate());
        self.setNo(0);
        self.settCapillary(0);
        self.setCapPh(0.0);
        self.setResPh(0.0);
        self.setCapillarySln("");
        self.setCapillaryConc(0.0);
        self.setReservoirSln("");
        self.setReservoirConc(0.0);
        self.settSealed(0);
        self.settSuppressed(0);
        self.setSampleFreq(0.0);
        self.setFilterFreq(0.0);
        self.setTranslocationsYN(0);
        self.setDescription("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Date = self._Connection.getDate(1);
        self._No = self._Connection.getInt(2);
        self._tCapillary = self._Connection.getInt(3);
        self._CapPh = self._Connection.getDouble(4);
        self._ResPh = self._Connection.getDouble(5);
        self._CapillarySln = self._Connection.getString(6);
        self._CapillaryConc = self._Connection.getDouble(7);
        self._ReservoirSln = self._Connection.getString(8);
        self._ReservoirConc = self._Connection.getDouble(9);
        self._tSealed = self._Connection.getInt(10);
        self._tSuppressed = self._Connection.getInt(11);
        self._SampleFreq = self._Connection.getDouble(12);
        self._FilterFreq = self._Connection.getDouble(13);
        self._TranslocationsYN = self._Connection.getInt(14);
        self._Description = self._Connection.getString(15);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Traces ( id int IDENTITY(1,1) NOT NULL , Date TEXT, No int, tCapillary int, CapPh REAL, ResPh REAL, CapillarySln TEXT, CapillaryConc REAL, ReservoirSln TEXT, ReservoirConc REAL, tSealed int, tSuppressed int, SampleFreq REAL, FilterFreq REAL, TranslocationsYN int, Description TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD Date TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD No int ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD tCapillary int ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD CapPh REAL ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD ResPh REAL ");
        if col == 6:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD CapillarySln TEXT ");
        if col == 7:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD CapillaryConc REAL ");
        if col == 8:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD ReservoirSln TEXT ");
        if col == 9:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD ReservoirConc REAL ");
        if col == 10:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD tSealed int ");
        if col == 11:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD tSuppressed int ");
        if col == 12:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD SampleFreq REAL ");
        if col == 13:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD FilterFreq REAL ");
        if col == 14:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD TranslocationsYN int ");
        if col == 15:
            self._Connection.ExecuteUpdate("ALTER TABLE Traces ADD Description TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Traces (Date , No , tCapillary , CapPh , ResPh , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , tSealed , tSuppressed , SampleFreq , FilterFreq , TranslocationsYN , Description  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )");
    def NextResult(self):
        if(self._Connection.NextResult()):
            self.LoadFromRs();
            return(True);
        else:
            return(False);
    def CloseConnection():
        self._Connection.CloseResults();
    #Select Methods --------------
    def SELECT(self, SearchPhrase):
        if type(SearchPhrase) == int:
            self._Connection.ExecuteQuery("Select * FROM Traces WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Traces WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Traces WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Traces SET Date =  ? , No =  ? , tCapillary =  ? , CapPh =  ? , ResPh =  ? , CapillarySln =  ? , CapillaryConc =  ? , ReservoirSln =  ? , ReservoirConc =  ? , tSealed =  ? , tSuppressed =  ? , SampleFreq =  ? , FilterFreq =  ? , TranslocationsYN =  ? , Description =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Traces SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Traces WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Traces");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Date' : self.getDate(),'No' : self.getNo(),'tCapillary' : self.gettCapillary(),'CapPh' : self.getCapPh(),'ResPh' : self.getResPh(),'CapillarySln' : self.getCapillarySln(),'CapillaryConc' : self.getCapillaryConc(),'ReservoirSln' : self.getReservoirSln(),'ReservoirConc' : self.getReservoirConc(),'tSealed' : self.gettSealed(),'tSuppressed' : self.gettSuppressed(),'SampleFreq' : self.getSampleFreq(),'FilterFreq' : self.getFilterFreq(),'TranslocationsYN' : self.getTranslocationsYN(),'Description' : self.getDescription()})
    def LoadRsToMemory(self):
        data = []
        self._Connection.count = 0
        while self.NextResult():
            data.append(self.to_dict())
        return(data);
    def dataFrame(self):
        import pandas as pd
        return(pd.DataFrame.from_dict(self.LoadRsToMemory(), orient = 'columns'))
    # To string method
    def __str__(self):
        return(self.toString())
    def toString(self):
        Ret = " ";
        Ret = Ret + " "+ str(self._id) + ", ";
        Ret = Ret + " "+ str(self._Date) + ", ";
        Ret = Ret + " "+ str(self._No) + ", ";
        Ret = Ret + " "+ str(self._tCapillary) + ", ";
        Ret = Ret + " "+ str(self._CapPh) + ", ";
        Ret = Ret + " "+ str(self._ResPh) + ", ";
        Ret = Ret + " "+ str(self._CapillarySln) + ", ";
        Ret = Ret + " "+ str(self._CapillaryConc) + ", ";
        Ret = Ret + " "+ str(self._ReservoirSln) + ", ";
        Ret = Ret + " "+ str(self._ReservoirConc) + ", ";
        Ret = Ret + " "+ str(self._tSealed) + ", ";
        Ret = Ret + " "+ str(self._tSuppressed) + ", ";
        Ret = Ret + " "+ str(self._SampleFreq) + ", ";
        Ret = Ret + " "+ str(self._FilterFreq) + ", ";
        Ret = Ret + " "+ str(self._TranslocationsYN) + ", ";
        Ret = Ret + " "+ str(self._Description) + ", ";
        return(Ret);
    # To JSON method
    def toJSON(self):
        return(toJSON(true)) ;
    def toJSON(Bracket):
        Ret = "";
        if(Bracket == true):
            Ret = "{";
        Ret = Ret + "\"id\":\"" + self._id +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Date\":\"" + self._Date +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"No\":\"" + self._No +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"tCapillary\":\"" + self._tCapillary +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapPh\":\"" + self._CapPh +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ResPh\":\"" + self._ResPh +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapillarySln\":\"" + self._CapillarySln +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapillaryConc\":\"" + self._CapillaryConc +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ReservoirSln\":\"" + self._ReservoirSln +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ReservoirConc\":\"" + self._ReservoirConc +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"tSealed\":\"" + self._tSealed +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"tSuppressed\":\"" + self._tSuppressed +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"SampleFreq\":\"" + self._SampleFreq +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"FilterFreq\":\"" + self._FilterFreq +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"TranslocationsYN\":\"" + self._TranslocationsYN +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Description\":\"" + self._Description +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

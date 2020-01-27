#  Interface for Experiments code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Experiments: #/*extends TableInterfaceBase*/
    TableName = "Experiments";
    
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
        self._isChanged_Capillary = False;
        self._isChanged_CapPh = False;
        self._isChanged_ResPh = False;
        self._isChanged_Voffset = False;
        self._isChanged_Ioffset = False;
        self._isChanged_Resistance = False;
        self._isChanged_LowRes = False;
        self._isChanged_HighRes = False;
        self._isChanged_nPerm = False;
        self._isChanged_pPerm = False;
        self._isChanged_PermOffset = False;
        self._isChanged_AnalysisDate = False;
        self._isChanged_CapillarySln = False;
        self._isChanged_CapillaryConc = False;
        self._isChanged_ReservoirSln = False;
        self._isChanged_ReservoirConc = False;
        self._isChanged_Sealed = False;
        self._isChanged_Suppressed = False;
        self._isChanged_FileType = False;
        self._isChanged_Comment = False;
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
    
    def setCapillary(self, Capillary):
        self._Capillary = Capillary;
        self._isChanged_Capillary = True;
    def getCapillary(self):
        return (self._Capillary)
    
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
    
    def setVoffset(self, Voffset):
        self._Voffset = Voffset;
        self._isChanged_Voffset = True;
    def getVoffset(self):
        return (self._Voffset)
    
    def setIoffset(self, Ioffset):
        self._Ioffset = Ioffset;
        self._isChanged_Ioffset = True;
    def getIoffset(self):
        return (self._Ioffset)
    
    def setResistance(self, Resistance):
        self._Resistance = Resistance;
        self._isChanged_Resistance = True;
    def getResistance(self):
        return (self._Resistance)
    
    def setLowRes(self, LowRes):
        self._LowRes = LowRes;
        self._isChanged_LowRes = True;
    def getLowRes(self):
        return (self._LowRes)
    
    def setHighRes(self, HighRes):
        self._HighRes = HighRes;
        self._isChanged_HighRes = True;
    def getHighRes(self):
        return (self._HighRes)
    
    def setnPerm(self, nPerm):
        self._nPerm = nPerm;
        self._isChanged_nPerm = True;
    def getnPerm(self):
        return (self._nPerm)
    
    def setpPerm(self, pPerm):
        self._pPerm = pPerm;
        self._isChanged_pPerm = True;
    def getpPerm(self):
        return (self._pPerm)
    
    def setPermOffset(self, PermOffset):
        self._PermOffset = PermOffset;
        self._isChanged_PermOffset = True;
    def getPermOffset(self):
        return (self._PermOffset)
    
    def setAnalysisDate(self, AnalysisDate):
        self._AnalysisDate = AnalysisDate;
        self._isChanged_AnalysisDate = True;
    def getAnalysisDate(self):
        return (self._AnalysisDate)
    
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
    
    def setSealed(self, Sealed):
        self._Sealed = Sealed;
        self._isChanged_Sealed = True;
    def getSealed(self):
        return (self._Sealed)
    
    def setSuppressed(self, Suppressed):
        self._Suppressed = Suppressed;
        self._isChanged_Suppressed = True;
    def getSuppressed(self):
        return (self._Suppressed)
    
    def setFileType(self, FileType):
        self._FileType = FileType;
        self._isChanged_FileType = True;
    def getFileType(self):
        return (self._FileType)
    
    def setComment(self, Comment):
        self._Comment = Comment;
        self._isChanged_Comment = True;
    def getComment(self):
        return (self._Comment)
    
    def Initialise(self):
        self.setid(0);
        self.setDate( DBDate());
        self.setNo(0);
        self.setCapillary(0);
        self.setCapPh(0.0);
        self.setResPh(0.0);
        self.setVoffset(0.0);
        self.setIoffset(0.0);
        self.setResistance(0.0);
        self.setLowRes(0.0);
        self.setHighRes(0.0);
        self.setnPerm(0.0);
        self.setpPerm(0.0);
        self.setPermOffset(0.0);
        self.setAnalysisDate(DBDateTime());
        self.setCapillarySln("");
        self.setCapillaryConc(0.0);
        self.setReservoirSln("");
        self.setReservoirConc(0.0);
        self.setSealed(0);
        self.setSuppressed(0);
        self.setFileType(0);
        self.setComment("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Date = self._Connection.getDate(1);
        self._No = self._Connection.getInt(2);
        self._Capillary = self._Connection.getInt(3);
        self._CapPh = self._Connection.getDouble(4);
        self._ResPh = self._Connection.getDouble(5);
        self._Voffset = self._Connection.getDouble(6);
        self._Ioffset = self._Connection.getDouble(7);
        self._Resistance = self._Connection.getDouble(8);
        self._LowRes = self._Connection.getDouble(9);
        self._HighRes = self._Connection.getDouble(10);
        self._nPerm = self._Connection.getDouble(11);
        self._pPerm = self._Connection.getDouble(12);
        self._PermOffset = self._Connection.getDouble(13);
        self._AnalysisDate = self._Connection.getTimestamp(14);
        self._CapillarySln = self._Connection.getString(15);
        self._CapillaryConc = self._Connection.getDouble(16);
        self._ReservoirSln = self._Connection.getString(17);
        self._ReservoirConc = self._Connection.getDouble(18);
        self._Sealed = self._Connection.getInt(19);
        self._Suppressed = self._Connection.getInt(20);
        self._FileType = self._Connection.getInt(21);
        self._Comment = self._Connection.getString(22);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Experiments ( id int IDENTITY(1,1) NOT NULL , Date TEXT, No int, Capillary int, CapPh REAL, ResPh REAL, Voffset REAL, Ioffset REAL, Resistance REAL, LowRes REAL, HighRes REAL, nPerm REAL, pPerm REAL, PermOffset REAL, AnalysisDate TEXT, CapillarySln TEXT, CapillaryConc REAL, ReservoirSln TEXT, ReservoirConc REAL, Sealed int, Suppressed int, FileType int, Comment TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Date TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD No int ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Capillary int ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD CapPh REAL ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD ResPh REAL ");
        if col == 6:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Voffset REAL ");
        if col == 7:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Ioffset REAL ");
        if col == 8:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Resistance REAL ");
        if col == 9:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD LowRes REAL ");
        if col == 10:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD HighRes REAL ");
        if col == 11:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD nPerm REAL ");
        if col == 12:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD pPerm REAL ");
        if col == 13:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD PermOffset REAL ");
        if col == 14:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD AnalysisDate TEXT ");
        if col == 15:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD CapillarySln TEXT ");
        if col == 16:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD CapillaryConc REAL ");
        if col == 17:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD ReservoirSln TEXT ");
        if col == 18:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD ReservoirConc REAL ");
        if col == 19:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Sealed int ");
        if col == 20:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Suppressed int ");
        if col == 21:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD FileType int ");
        if col == 22:
            self._Connection.ExecuteUpdate("ALTER TABLE Experiments ADD Comment TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Experiments (Date , No , Capillary , CapPh , ResPh , Voffset , Ioffset , Resistance , LowRes , HighRes , nPerm , pPerm , PermOffset , AnalysisDate , CapillarySln , CapillaryConc , ReservoirSln , ReservoirConc , Sealed , Suppressed , FileType , Comment  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM Experiments WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Experiments WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Experiments WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Experiments SET Date =  ? , No =  ? , Capillary =  ? , CapPh =  ? , ResPh =  ? , Voffset =  ? , Ioffset =  ? , Resistance =  ? , LowRes =  ? , HighRes =  ? , nPerm =  ? , pPerm =  ? , PermOffset =  ? , AnalysisDate =  ? , CapillarySln =  ? , CapillaryConc =  ? , ReservoirSln =  ? , ReservoirConc =  ? , Sealed =  ? , Suppressed =  ? , FileType =  ? , Comment =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Experiments SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Experiments WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Experiments");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Date' : self.getDate(),'No' : self.getNo(),'Capillary' : self.getCapillary(),'CapPh' : self.getCapPh(),'ResPh' : self.getResPh(),'Voffset' : self.getVoffset(),'Ioffset' : self.getIoffset(),'Resistance' : self.getResistance(),'LowRes' : self.getLowRes(),'HighRes' : self.getHighRes(),'nPerm' : self.getnPerm(),'pPerm' : self.getpPerm(),'PermOffset' : self.getPermOffset(),'AnalysisDate' : self.getAnalysisDate(),'CapillarySln' : self.getCapillarySln(),'CapillaryConc' : self.getCapillaryConc(),'ReservoirSln' : self.getReservoirSln(),'ReservoirConc' : self.getReservoirConc(),'Sealed' : self.getSealed(),'Suppressed' : self.getSuppressed(),'FileType' : self.getFileType(),'Comment' : self.getComment()})
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
        Ret = Ret + " "+ str(self._Capillary) + ", ";
        Ret = Ret + " "+ str(self._CapPh) + ", ";
        Ret = Ret + " "+ str(self._ResPh) + ", ";
        Ret = Ret + " "+ str(self._Voffset) + ", ";
        Ret = Ret + " "+ str(self._Ioffset) + ", ";
        Ret = Ret + " "+ str(self._Resistance) + ", ";
        Ret = Ret + " "+ str(self._LowRes) + ", ";
        Ret = Ret + " "+ str(self._HighRes) + ", ";
        Ret = Ret + " "+ str(self._nPerm) + ", ";
        Ret = Ret + " "+ str(self._pPerm) + ", ";
        Ret = Ret + " "+ str(self._PermOffset) + ", ";
        Ret = Ret + " "+ str(self._AnalysisDate) + ", ";
        Ret = Ret + " "+ str(self._CapillarySln) + ", ";
        Ret = Ret + " "+ str(self._CapillaryConc) + ", ";
        Ret = Ret + " "+ str(self._ReservoirSln) + ", ";
        Ret = Ret + " "+ str(self._ReservoirConc) + ", ";
        Ret = Ret + " "+ str(self._Sealed) + ", ";
        Ret = Ret + " "+ str(self._Suppressed) + ", ";
        Ret = Ret + " "+ str(self._FileType) + ", ";
        Ret = Ret + " "+ str(self._Comment) + ", ";
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
        Ret = Ret + "\"Capillary\":\"" + self._Capillary +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapPh\":\"" + self._CapPh +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ResPh\":\"" + self._ResPh +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Voffset\":\"" + self._Voffset +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Ioffset\":\"" + self._Ioffset +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Resistance\":\"" + self._Resistance +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"LowRes\":\"" + self._LowRes +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"HighRes\":\"" + self._HighRes +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"nPerm\":\"" + self._nPerm +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"pPerm\":\"" + self._pPerm +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"PermOffset\":\"" + self._PermOffset +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"AnalysisDate\":\"" + self._AnalysisDate +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapillarySln\":\"" + self._CapillarySln +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapillaryConc\":\"" + self._CapillaryConc +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ReservoirSln\":\"" + self._ReservoirSln +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ReservoirConc\":\"" + self._ReservoirConc +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Sealed\":\"" + self._Sealed +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Suppressed\":\"" + self._Suppressed +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"FileType\":\"" + self._FileType +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Comment\":\"" + self._Comment +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

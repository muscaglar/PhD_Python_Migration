#  Interface for AnalysisValues code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class AnalysisValues: #/*extends TableInterfaceBase*/
    TableName = "AnalysisValues";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Name = False;
        self._isChanged_Value = False;
        self._isChanged_StringValue = False;
        self._isChanged_Trace = False;
        self._isChanged_Expt = False;
        self._isChanged_UpdateDate = False;
        self._isChanged_nvCapillary = False;
        self._isChanged_Spectra = False;
    #Access Methods to set and Read Fields --------------
    def setid(self, id):
        self._id = id;
        self._isChanged_id = True;
    def getid(self):
        return (self._id)
    
    def setName(self, Name):
        self._Name = Name;
        self._isChanged_Name = True;
    def getName(self):
        return (self._Name)
    
    def setValue(self, Value):
        self._Value = Value;
        self._isChanged_Value = True;
    def getValue(self):
        return (self._Value)
    
    def setStringValue(self, StringValue):
        self._StringValue = StringValue;
        self._isChanged_StringValue = True;
    def getStringValue(self):
        return (self._StringValue)
    
    def setTrace(self, Trace):
        self._Trace = Trace;
        self._isChanged_Trace = True;
    def getTrace(self):
        return (self._Trace)
    
    def setExpt(self, Expt):
        self._Expt = Expt;
        self._isChanged_Expt = True;
    def getExpt(self):
        return (self._Expt)
    
    def setUpdateDate(self, UpdateDate):
        self._UpdateDate = UpdateDate;
        self._isChanged_UpdateDate = True;
    def getUpdateDate(self):
        return (self._UpdateDate)
    
    def setnvCapillary(self, nvCapillary):
        self._nvCapillary = nvCapillary;
        self._isChanged_nvCapillary = True;
    def getnvCapillary(self):
        return (self._nvCapillary)
    
    def setSpectra(self, Spectra):
        self._Spectra = Spectra;
        self._isChanged_Spectra = True;
    def getSpectra(self):
        return (self._Spectra)
    
    def Initialise(self):
        self.setid(0);
        self.setName("");
        self.setValue(0.0);
        self.setStringValue("");
        self.setTrace(0);
        self.setExpt(0);
        self.setUpdateDate(DBDateTime());
        self.setnvCapillary(0);
        self.setSpectra(0);
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Name = self._Connection.getString(1);
        self._Value = self._Connection.getDouble(2);
        self._StringValue = self._Connection.getString(3);
        self._Trace = self._Connection.getInt(4);
        self._Expt = self._Connection.getInt(5);
        self._UpdateDate = self._Connection.getTimestamp(6);
        self._nvCapillary = self._Connection.getInt(7);
        self._Spectra = self._Connection.getInt(8);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE AnalysisValues ( id int IDENTITY(1,1) NOT NULL , Name TEXT, Value REAL, StringValue TEXT, Trace int, Expt int, UpdateDate TEXT, nvCapillary int, Spectra int )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD Name TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD Value REAL ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD StringValue TEXT ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD Trace int ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD Expt int ");
        if col == 6:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD UpdateDate TEXT ");
        if col == 7:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD nvCapillary int ");
        if col == 8:
            self._Connection.ExecuteUpdate("ALTER TABLE AnalysisValues ADD Spectra int ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO AnalysisValues (Name , Value , StringValue , Trace , Expt , UpdateDate , nvCapillary , Spectra  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM AnalysisValues WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM AnalysisValues WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM AnalysisValues WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE AnalysisValues SET Name =  ? , Value =  ? , StringValue =  ? , Trace =  ? , Expt =  ? , UpdateDate =  ? , nvCapillary =  ? , Spectra =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE AnalysisValues SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM AnalysisValues WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE AnalysisValues");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Name' : self.getName(),'Value' : self.getValue(),'StringValue' : self.getStringValue(),'Trace' : self.getTrace(),'Expt' : self.getExpt(),'UpdateDate' : self.getUpdateDate(),'nvCapillary' : self.getnvCapillary(),'Spectra' : self.getSpectra()})
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
        Ret = Ret + " "+ str(self._Name) + ", ";
        Ret = Ret + " "+ str(self._Value) + ", ";
        Ret = Ret + " "+ str(self._StringValue) + ", ";
        Ret = Ret + " "+ str(self._Trace) + ", ";
        Ret = Ret + " "+ str(self._Expt) + ", ";
        Ret = Ret + " "+ str(self._UpdateDate) + ", ";
        Ret = Ret + " "+ str(self._nvCapillary) + ", ";
        Ret = Ret + " "+ str(self._Spectra) + ", ";
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
        Ret = Ret + "\"Name\":\"" + self._Name +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Value\":\"" + self._Value +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"StringValue\":\"" + self._StringValue +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Trace\":\"" + self._Trace +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Expt\":\"" + self._Expt +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"UpdateDate\":\"" + self._UpdateDate +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"nvCapillary\":\"" + self._nvCapillary +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Spectra\":\"" + self._Spectra +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

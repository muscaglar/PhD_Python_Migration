#  Interface for Capillaries code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Capillaries: #/*extends TableInterfaceBase*/
    TableName = "Capillaries";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Date = False;
        self._isChanged_Type = False;
        self._isChanged_CapNo = False;
        self._isChanged_ExptType = False;
        self._isChanged_investigator = False;
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
    
    def setType(self, Type):
        self._Type = Type;
        self._isChanged_Type = True;
    def getType(self):
        return (self._Type)
    
    def setCapNo(self, CapNo):
        self._CapNo = CapNo;
        self._isChanged_CapNo = True;
    def getCapNo(self):
        return (self._CapNo)
    
    def setExptType(self, ExptType):
        self._ExptType = ExptType;
        self._isChanged_ExptType = True;
    def getExptType(self):
        return (self._ExptType)
    
    def setinvestigator(self, investigator):
        self._investigator = investigator;
        self._isChanged_investigator = True;
    def getinvestigator(self):
        return (self._investigator)
    
    def Initialise(self):
        self.setid(0);
        self.setDate( DBDate());
        self.setType("");
        self.setCapNo(0);
        self.setExptType("");
        self.setinvestigator(0);
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Date = self._Connection.getDate(1);
        self._Type = self._Connection.getString(2);
        self._CapNo = self._Connection.getInt(3);
        self._ExptType = self._Connection.getString(4);
        self._investigator = self._Connection.getInt(5);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Capillaries ( id int IDENTITY(1,1) NOT NULL , Date TEXT, Type TEXT, CapNo int, ExptType TEXT, investigator int )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Capillaries ADD Date TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Capillaries ADD Type TEXT ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Capillaries ADD CapNo int ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Capillaries ADD ExptType TEXT ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE Capillaries ADD investigator int ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Capillaries (Date , Type , CapNo , ExptType , investigator  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM Capillaries WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Capillaries WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Capillaries WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Capillaries SET Date =  ? , Type =  ? , CapNo =  ? , ExptType =  ? , investigator =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Capillaries SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Capillaries WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Capillaries");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Date' : self.getDate(),'Type' : self.getType(),'CapNo' : self.getCapNo(),'ExptType' : self.getExptType(),'investigator' : self.getinvestigator()})
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
        Ret = Ret + " "+ str(self._Type) + ", ";
        Ret = Ret + " "+ str(self._CapNo) + ", ";
        Ret = Ret + " "+ str(self._ExptType) + ", ";
        Ret = Ret + " "+ str(self._investigator) + ", ";
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
        Ret = Ret + "\"Type\":\"" + self._Type +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"CapNo\":\"" + self._CapNo +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ExptType\":\"" + self._ExptType +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"investigator\":\"" + self._investigator +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

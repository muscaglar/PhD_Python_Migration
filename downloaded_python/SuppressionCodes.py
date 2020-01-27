#  Interface for SuppressionCodes code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class SuppressionCodes: #/*extends TableInterfaceBase*/
    TableName = "SuppressionCodes";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Name = False;
        self._isChanged_Details = False;
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
    
    def setDetails(self, Details):
        self._Details = Details;
        self._isChanged_Details = True;
    def getDetails(self):
        return (self._Details)
    
    def Initialise(self):
        self.setid(0);
        self.setName("");
        self.setDetails("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Name = self._Connection.getString(1);
        self._Details = self._Connection.getString(2);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE SuppressionCodes ( id int IDENTITY(1,1) NOT NULL , Name TEXT, Details TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE SuppressionCodes ADD Name TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE SuppressionCodes ADD Details TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO SuppressionCodes (Name , Details  ) VALUES ( ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM SuppressionCodes WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM SuppressionCodes WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM SuppressionCodes WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE SuppressionCodes SET Name =  ? , Details =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE SuppressionCodes SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM SuppressionCodes WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE SuppressionCodes");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Name' : self.getName(),'Details' : self.getDetails()})
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
        Ret = Ret + " "+ str(self._Details) + ", ";
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
        Ret = Ret + "\"Details\":\"" + self._Details +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

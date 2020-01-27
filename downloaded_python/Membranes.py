#  Interface for Membranes code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Membranes: #/*extends TableInterfaceBase*/
    TableName = "Membranes";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Material = False;
        self._isChanged_Name = False;
        self._isChanged_DateStarted = False;
        self._isChanged_Details = False;
    #Access Methods to set and Read Fields --------------
    def setid(self, id):
        self._id = id;
        self._isChanged_id = True;
    def getid(self):
        return (self._id)
    
    def setMaterial(self, Material):
        self._Material = Material;
        self._isChanged_Material = True;
    def getMaterial(self):
        return (self._Material)
    
    def setName(self, Name):
        self._Name = Name;
        self._isChanged_Name = True;
    def getName(self):
        return (self._Name)
    
    def setDateStarted(self, DateStarted):
        self._DateStarted = DateStarted;
        self._isChanged_DateStarted = True;
    def getDateStarted(self):
        return (self._DateStarted)
    
    def setDetails(self, Details):
        self._Details = Details;
        self._isChanged_Details = True;
    def getDetails(self):
        return (self._Details)
    
    def Initialise(self):
        self.setid(0);
        self.setMaterial("");
        self.setName("");
        self.setDateStarted( DBDate());
        self.setDetails("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Material = self._Connection.getString(1);
        self._Name = self._Connection.getString(2);
        self._DateStarted = self._Connection.getDate(3);
        self._Details = self._Connection.getString(4);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Membranes ( id int IDENTITY(1,1) NOT NULL , Material TEXT, Name TEXT, DateStarted TEXT, Details TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Membranes ADD Material TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Membranes ADD Name TEXT ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Membranes ADD DateStarted TEXT ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Membranes ADD Details TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Membranes (Material , Name , DateStarted , Details  ) VALUES ( ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM Membranes WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Membranes WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Membranes WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Membranes SET Material =  ? , Name =  ? , DateStarted =  ? , Details =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Membranes SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Membranes WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Membranes");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Material' : self.getMaterial(),'Name' : self.getName(),'DateStarted' : self.getDateStarted(),'Details' : self.getDetails()})
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
        Ret = Ret + " "+ str(self._Material) + ", ";
        Ret = Ret + " "+ str(self._Name) + ", ";
        Ret = Ret + " "+ str(self._DateStarted) + ", ";
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
        Ret = Ret + "\"Material\":\"" + self._Material +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Name\":\"" + self._Name +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"DateStarted\":\"" + self._DateStarted +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Details\":\"" + self._Details +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

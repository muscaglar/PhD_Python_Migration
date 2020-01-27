#  Interface for FileTypes code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class FileTypes: #/*extends TableInterfaceBase*/
    TableName = "FileTypes";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_Type = False;
        self._isChanged_Details = False;
        self._isChanged_Extension = False;
    #Access Methods to set and Read Fields --------------
    def setid(self, id):
        self._id = id;
        self._isChanged_id = True;
    def getid(self):
        return (self._id)
    
    def setType(self, Type):
        self._Type = Type;
        self._isChanged_Type = True;
    def getType(self):
        return (self._Type)
    
    def setDetails(self, Details):
        self._Details = Details;
        self._isChanged_Details = True;
    def getDetails(self):
        return (self._Details)
    
    def setExtension(self, Extension):
        self._Extension = Extension;
        self._isChanged_Extension = True;
    def getExtension(self):
        return (self._Extension)
    
    def Initialise(self):
        self.setid(0);
        self.setType("");
        self.setDetails("");
        self.setExtension("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Type = self._Connection.getString(1);
        self._Details = self._Connection.getString(2);
        self._Extension = self._Connection.getString(3);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE FileTypes ( id int IDENTITY(1,1) NOT NULL , Type TEXT, Details TEXT, Extension TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE FileTypes ADD Type TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE FileTypes ADD Details TEXT ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE FileTypes ADD Extension TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO FileTypes (Type , Details , Extension  ) VALUES ( ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM FileTypes WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM FileTypes WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM FileTypes WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE FileTypes SET Type =  ? , Details =  ? , Extension =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE FileTypes SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM FileTypes WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE FileTypes");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Type' : self.getType(),'Details' : self.getDetails(),'Extension' : self.getExtension()})
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
        Ret = Ret + " "+ str(self._Type) + ", ";
        Ret = Ret + " "+ str(self._Details) + ", ";
        Ret = Ret + " "+ str(self._Extension) + ", ";
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
        Ret = Ret + "\"Type\":\"" + self._Type +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Details\":\"" + self._Details +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Extension\":\"" + self._Extension +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

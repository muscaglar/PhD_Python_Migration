#  Interface for Investigators code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Investigators: #/*extends TableInterfaceBase*/
    TableName = "Investigators";
    
    def __init__(self,  Connection, id=None):
        self._Connection = Connection;
        self.Initialise()
        if id != None:
            self.SELECT(id);
    #Members to Match fields in table -----------------
    def ClearIsChanged(self):
        self._isChanged_id = False;
        self._isChanged_DateStarted = False;
        self._isChanged_Surname = False;
        self._isChanged_Forename = False;
        self._isChanged_PulicationName = False;
        self._isChanged_orcid = False;
        self._isChanged_emailaddress = False;
        self._isChanged_Crsid = False;
        self._isChanged_Institution = False;
    #Access Methods to set and Read Fields --------------
    def setid(self, id):
        self._id = id;
        self._isChanged_id = True;
    def getid(self):
        return (self._id)
    
    def setDateStarted(self, DateStarted):
        self._DateStarted = DateStarted;
        self._isChanged_DateStarted = True;
    def getDateStarted(self):
        return (self._DateStarted)
    
    def setSurname(self, Surname):
        self._Surname = Surname;
        self._isChanged_Surname = True;
    def getSurname(self):
        return (self._Surname)
    
    def setForename(self, Forename):
        self._Forename = Forename;
        self._isChanged_Forename = True;
    def getForename(self):
        return (self._Forename)
    
    def setPulicationName(self, PulicationName):
        self._PulicationName = PulicationName;
        self._isChanged_PulicationName = True;
    def getPulicationName(self):
        return (self._PulicationName)
    
    def setorcid(self, orcid):
        self._orcid = orcid;
        self._isChanged_orcid = True;
    def getorcid(self):
        return (self._orcid)
    
    def setemailaddress(self, emailaddress):
        self._emailaddress = emailaddress;
        self._isChanged_emailaddress = True;
    def getemailaddress(self):
        return (self._emailaddress)
    
    def setCrsid(self, Crsid):
        self._Crsid = Crsid;
        self._isChanged_Crsid = True;
    def getCrsid(self):
        return (self._Crsid)
    
    def setInstitution(self, Institution):
        self._Institution = Institution;
        self._isChanged_Institution = True;
    def getInstitution(self):
        return (self._Institution)
    
    def Initialise(self):
        self.setid(0);
        self.setDateStarted( DBDate());
        self.setSurname("");
        self.setForename("");
        self.setPulicationName("");
        self.setorcid("");
        self.setemailaddress("");
        self.setCrsid("");
        self.setInstitution("");
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._DateStarted = self._Connection.getDate(1);
        self._Surname = self._Connection.getString(2);
        self._Forename = self._Connection.getString(3);
        self._PulicationName = self._Connection.getString(4);
        self._orcid = self._Connection.getString(5);
        self._emailaddress = self._Connection.getString(6);
        self._Crsid = self._Connection.getString(7);
        self._Institution = self._Connection.getString(8);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Investigators ( id int IDENTITY(1,1) NOT NULL , DateStarted TEXT, Surname TEXT, Forename TEXT, PulicationName TEXT, orcid TEXT, emailaddress TEXT, Crsid TEXT, Institution TEXT )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD DateStarted TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD Surname TEXT ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD Forename TEXT ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD PulicationName TEXT ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD orcid TEXT ");
        if col == 6:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD emailaddress TEXT ");
        if col == 7:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD Crsid TEXT ");
        if col == 8:
            self._Connection.ExecuteUpdate("ALTER TABLE Investigators ADD Institution TEXT ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Investigators (DateStarted , Surname , Forename , PulicationName , orcid , emailaddress , Crsid , Institution  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM Investigators WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Investigators WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Investigators WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Investigators SET DateStarted =  ? , Surname =  ? , Forename =  ? , PulicationName =  ? , orcid =  ? , emailaddress =  ? , Crsid =  ? , Institution =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Investigators SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Investigators WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Investigators");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'DateStarted' : self.getDateStarted(),'Surname' : self.getSurname(),'Forename' : self.getForename(),'PulicationName' : self.getPulicationName(),'orcid' : self.getorcid(),'emailaddress' : self.getemailaddress(),'Crsid' : self.getCrsid(),'Institution' : self.getInstitution()})
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
        Ret = Ret + " "+ str(self._DateStarted) + ", ";
        Ret = Ret + " "+ str(self._Surname) + ", ";
        Ret = Ret + " "+ str(self._Forename) + ", ";
        Ret = Ret + " "+ str(self._PulicationName) + ", ";
        Ret = Ret + " "+ str(self._orcid) + ", ";
        Ret = Ret + " "+ str(self._emailaddress) + ", ";
        Ret = Ret + " "+ str(self._Crsid) + ", ";
        Ret = Ret + " "+ str(self._Institution) + ", ";
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
        Ret = Ret + "\"DateStarted\":\"" + self._DateStarted +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Surname\":\"" + self._Surname +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Forename\":\"" + self._Forename +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"PulicationName\":\"" + self._PulicationName +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"orcid\":\"" + self._orcid +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"emailaddress\":\"" + self._emailaddress +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Crsid\":\"" + self._Crsid +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Institution\":\"" + self._Institution +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

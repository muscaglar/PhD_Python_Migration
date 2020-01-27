#  Interface for Spectra code for :
# (c) Michael Walker
# www.michael-walker.co.uk
# Code auto generated



from DBConnection_ExptsDB import DBConnection_ExptsDB
from DBSupportLib import *
class Spectra: #/*extends TableInterfaceBase*/
    TableName = "Spectra";
    
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
        self._isChanged_sCapillary = False;
        self._isChanged_Membrane = False;
        self._isChanged_MembraneName = False;
        self._isChanged_Loc2D = False;
        self._isChanged_Scale2D = False;
        self._isChanged_Area2D = False;
        self._isChanged_Height2D = False;
        self._isChanged_LocD = False;
        self._isChanged_ScaleD = False;
        self._isChanged_AreaD = False;
        self._isChanged_HeightD = False;
        self._isChanged_LocG = False;
        self._isChanged_ScaleG = False;
        self._isChanged_AreaG = False;
        self._isChanged_HeightG = False;
        self._isChanged_LocDDp = False;
        self._isChanged_ScaleDDp = False;
        self._isChanged_AreaDDp = False;
        self._isChanged_HeightDDp = False;
        self._isChanged_AnalysisDate = False;
        self._isChanged_RatioD2D = False;
        self._isChanged_RatioD2G = False;
        self._isChanged_Ratio2DG = False;
        self._isChanged_NoLayers = False;
        self._isChanged_Comment = False;
        self._isChanged_SInvestigator = False;
        self._isChanged_sSuppressed = False;
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
    
    def setsCapillary(self, sCapillary):
        self._sCapillary = sCapillary;
        self._isChanged_sCapillary = True;
    def getsCapillary(self):
        return (self._sCapillary)
    
    def setMembrane(self, Membrane):
        self._Membrane = Membrane;
        self._isChanged_Membrane = True;
    def getMembrane(self):
        return (self._Membrane)
    
    def setMembraneName(self, MembraneName):
        self._MembraneName = MembraneName;
        self._isChanged_MembraneName = True;
    def getMembraneName(self):
        return (self._MembraneName)
    
    def setLoc2D(self, Loc2D):
        self._Loc2D = Loc2D;
        self._isChanged_Loc2D = True;
    def getLoc2D(self):
        return (self._Loc2D)
    
    def setScale2D(self, Scale2D):
        self._Scale2D = Scale2D;
        self._isChanged_Scale2D = True;
    def getScale2D(self):
        return (self._Scale2D)
    
    def setArea2D(self, Area2D):
        self._Area2D = Area2D;
        self._isChanged_Area2D = True;
    def getArea2D(self):
        return (self._Area2D)
    
    def setHeight2D(self, Height2D):
        self._Height2D = Height2D;
        self._isChanged_Height2D = True;
    def getHeight2D(self):
        return (self._Height2D)
    
    def setLocD(self, LocD):
        self._LocD = LocD;
        self._isChanged_LocD = True;
    def getLocD(self):
        return (self._LocD)
    
    def setScaleD(self, ScaleD):
        self._ScaleD = ScaleD;
        self._isChanged_ScaleD = True;
    def getScaleD(self):
        return (self._ScaleD)
    
    def setAreaD(self, AreaD):
        self._AreaD = AreaD;
        self._isChanged_AreaD = True;
    def getAreaD(self):
        return (self._AreaD)
    
    def setHeightD(self, HeightD):
        self._HeightD = HeightD;
        self._isChanged_HeightD = True;
    def getHeightD(self):
        return (self._HeightD)
    
    def setLocG(self, LocG):
        self._LocG = LocG;
        self._isChanged_LocG = True;
    def getLocG(self):
        return (self._LocG)
    
    def setScaleG(self, ScaleG):
        self._ScaleG = ScaleG;
        self._isChanged_ScaleG = True;
    def getScaleG(self):
        return (self._ScaleG)
    
    def setAreaG(self, AreaG):
        self._AreaG = AreaG;
        self._isChanged_AreaG = True;
    def getAreaG(self):
        return (self._AreaG)
    
    def setHeightG(self, HeightG):
        self._HeightG = HeightG;
        self._isChanged_HeightG = True;
    def getHeightG(self):
        return (self._HeightG)
    
    def setLocDDp(self, LocDDp):
        self._LocDDp = LocDDp;
        self._isChanged_LocDDp = True;
    def getLocDDp(self):
        return (self._LocDDp)
    
    def setScaleDDp(self, ScaleDDp):
        self._ScaleDDp = ScaleDDp;
        self._isChanged_ScaleDDp = True;
    def getScaleDDp(self):
        return (self._ScaleDDp)
    
    def setAreaDDp(self, AreaDDp):
        self._AreaDDp = AreaDDp;
        self._isChanged_AreaDDp = True;
    def getAreaDDp(self):
        return (self._AreaDDp)
    
    def setHeightDDp(self, HeightDDp):
        self._HeightDDp = HeightDDp;
        self._isChanged_HeightDDp = True;
    def getHeightDDp(self):
        return (self._HeightDDp)
    
    def setAnalysisDate(self, AnalysisDate):
        self._AnalysisDate = AnalysisDate;
        self._isChanged_AnalysisDate = True;
    def getAnalysisDate(self):
        return (self._AnalysisDate)
    
    def setRatioD2D(self, RatioD2D):
        self._RatioD2D = RatioD2D;
        self._isChanged_RatioD2D = True;
    def getRatioD2D(self):
        return (self._RatioD2D)
    
    def setRatioD2G(self, RatioD2G):
        self._RatioD2G = RatioD2G;
        self._isChanged_RatioD2G = True;
    def getRatioD2G(self):
        return (self._RatioD2G)
    
    def setRatio2DG(self, Ratio2DG):
        self._Ratio2DG = Ratio2DG;
        self._isChanged_Ratio2DG = True;
    def getRatio2DG(self):
        return (self._Ratio2DG)
    
    def setNoLayers(self, NoLayers):
        self._NoLayers = NoLayers;
        self._isChanged_NoLayers = True;
    def getNoLayers(self):
        return (self._NoLayers)
    
    def setComment(self, Comment):
        self._Comment = Comment;
        self._isChanged_Comment = True;
    def getComment(self):
        return (self._Comment)
    
    def setSInvestigator(self, SInvestigator):
        self._SInvestigator = SInvestigator;
        self._isChanged_SInvestigator = True;
    def getSInvestigator(self):
        return (self._SInvestigator)
    
    def setsSuppressed(self, sSuppressed):
        self._sSuppressed = sSuppressed;
        self._isChanged_sSuppressed = True;
    def getsSuppressed(self):
        return (self._sSuppressed)
    
    def Initialise(self):
        self.setid(0);
        self.setDate( DBDate());
        self.setNo(0);
        self.setsCapillary(0);
        self.setMembrane(0);
        self.setMembraneName("");
        self.setLoc2D(0.0);
        self.setScale2D(0.0);
        self.setArea2D(0.0);
        self.setHeight2D(0.0);
        self.setLocD(0.0);
        self.setScaleD(0.0);
        self.setAreaD(0.0);
        self.setHeightD(0.0);
        self.setLocG(0.0);
        self.setScaleG(0.0);
        self.setAreaG(0.0);
        self.setHeightG(0.0);
        self.setLocDDp(0.0);
        self.setScaleDDp(0.0);
        self.setAreaDDp(0.0);
        self.setHeightDDp(0.0);
        self.setAnalysisDate(DBDateTime());
        self.setRatioD2D(0.0);
        self.setRatioD2G(0.0);
        self.setRatio2DG(0.0);
        self.setNoLayers(0.0);
        self.setComment("");
        self.setSInvestigator(0);
        self.setsSuppressed(0);
        self.ClearIsChanged();
    def LoadFromRs(self):
        self._id = self._Connection.getInt(0);
        self._Date = self._Connection.getDate(1);
        self._No = self._Connection.getInt(2);
        self._sCapillary = self._Connection.getInt(3);
        self._Membrane = self._Connection.getInt(4);
        self._MembraneName = self._Connection.getString(5);
        self._Loc2D = self._Connection.getDouble(6);
        self._Scale2D = self._Connection.getDouble(7);
        self._Area2D = self._Connection.getDouble(8);
        self._Height2D = self._Connection.getDouble(9);
        self._LocD = self._Connection.getDouble(10);
        self._ScaleD = self._Connection.getDouble(11);
        self._AreaD = self._Connection.getDouble(12);
        self._HeightD = self._Connection.getDouble(13);
        self._LocG = self._Connection.getDouble(14);
        self._ScaleG = self._Connection.getDouble(15);
        self._AreaG = self._Connection.getDouble(16);
        self._HeightG = self._Connection.getDouble(17);
        self._LocDDp = self._Connection.getDouble(18);
        self._ScaleDDp = self._Connection.getDouble(19);
        self._AreaDDp = self._Connection.getDouble(20);
        self._HeightDDp = self._Connection.getDouble(21);
        self._AnalysisDate = self._Connection.getTimestamp(22);
        self._RatioD2D = self._Connection.getDouble(23);
        self._RatioD2G = self._Connection.getDouble(24);
        self._Ratio2DG = self._Connection.getDouble(25);
        self._NoLayers = self._Connection.getDouble(26);
        self._Comment = self._Connection.getString(27);
        self._SInvestigator = self._Connection.getInt(28);
        self._sSuppressed = self._Connection.getInt(29);
    #Create Method --------------
    def CREATE(self):
        self._Connection.ExecuteUpdate("CREATE TABLE Spectra ( id int IDENTITY(1,1) NOT NULL , Date TEXT, No int, sCapillary int, Membrane int, MembraneName TEXT, Loc2D REAL, Scale2D REAL, Area2D REAL, Height2D REAL, LocD REAL, ScaleD REAL, AreaD REAL, HeightD REAL, LocG REAL, ScaleG REAL, AreaG REAL, HeightG REAL, LocDDp REAL, ScaleDDp REAL, AreaDDp REAL, HeightDDp REAL, AnalysisDate TEXT, RatioD2D REAL, RatioD2G REAL, Ratio2DG REAL, NoLayers REAL, Comment TEXT, SInvestigator int, sSuppressed int )");
    #Alter Method --------------
    def ALTER(self, Col):
        if col == 1:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Date TEXT ");
        if col == 2:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD No int ");
        if col == 3:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD sCapillary int ");
        if col == 4:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Membrane int ");
        if col == 5:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD MembraneName TEXT ");
        if col == 6:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Loc2D REAL ");
        if col == 7:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Scale2D REAL ");
        if col == 8:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Area2D REAL ");
        if col == 9:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Height2D REAL ");
        if col == 10:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD LocD REAL ");
        if col == 11:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD ScaleD REAL ");
        if col == 12:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD AreaD REAL ");
        if col == 13:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD HeightD REAL ");
        if col == 14:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD LocG REAL ");
        if col == 15:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD ScaleG REAL ");
        if col == 16:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD AreaG REAL ");
        if col == 17:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD HeightG REAL ");
        if col == 18:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD LocDDp REAL ");
        if col == 19:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD ScaleDDp REAL ");
        if col == 20:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD AreaDDp REAL ");
        if col == 21:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD HeightDDp REAL ");
        if col == 22:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD AnalysisDate TEXT ");
        if col == 23:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD RatioD2D REAL ");
        if col == 24:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD RatioD2G REAL ");
        if col == 25:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Ratio2DG REAL ");
        if col == 26:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD NoLayers REAL ");
        if col == 27:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD Comment TEXT ");
        if col == 28:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD SInvestigator int ");
        if col == 29:
            self._Connection.ExecuteUpdate("ALTER TABLE Spectra ADD sSuppressed int ");
    #Insert Method --------------
    def INSERT(self):
        self._Connection.ExecuteUpdate("INSERT INTO Spectra (Date , No , sCapillary , Membrane , MembraneName , Loc2D , Scale2D , Area2D , Height2D , LocD , ScaleD , AreaD , HeightD , LocG , ScaleG , AreaG , HeightG , LocDDp , ScaleDDp , AreaDDp , HeightDDp , AnalysisDate , RatioD2D , RatioD2G , Ratio2DG , NoLayers , Comment , SInvestigator , sSuppressed  ) VALUES ( ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ? ,  ?  )");
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
            self._Connection.ExecuteQuery("Select * FROM Spectra WHERE "+ "id = "+ str(SearchPhrase)+"");
        else:
            self._Connection.ExecuteQuery("Select * FROM Spectra WHERE "+SearchPhrase+"");
        if ( self._Connection.NextResult() ) :
            self.LoadFromRs();
        return(0);
    def SELECTsort(self, SearchPhrase, SortPhrase):
        self._Connection.ExecuteQuery("Select * FROM Spectra WHERE "+SearchPhrase+" ORDER BY "+SortPhrase+"");
        if ( self._Connection.NextResult() ):
            self.LoadFromRs();
        return(0);
    #Update Methods --------------
    #Update all
    def UPDATE(self):
        self._Connection.ExecuteUpdate("UPDATE Spectra SET Date =  ? , No =  ? , sCapillary =  ? , Membrane =  ? , MembraneName =  ? , Loc2D =  ? , Scale2D =  ? , Area2D =  ? , Height2D =  ? , LocD =  ? , ScaleD =  ? , AreaD =  ? , HeightD =  ? , LocG =  ? , ScaleG =  ? , AreaG =  ? , HeightG =  ? , LocDDp =  ? , ScaleDDp =  ? , AreaDDp =  ? , HeightDDp =  ? , AnalysisDate =  ? , RatioD2D =  ? , RatioD2G =  ? , Ratio2DG =  ? , NoLayers =  ? , Comment =  ? , SInvestigator =  ? , sSuppressed =  ?   WHERE  id = "+_id+";");
    #Update only the given column
    def UPDATE(self, Col):
        self._Connection.ExecuteUpdate("UPDATE Spectra SET Col =  '"+_Col+"'  WHERE  id = "+Col+"");
    # Delete methods --------------
    # Delete this entry - note coud check none 0.
    def DELETE(self):
        self._Connection.ExecuteUpdate("DELETE FROM Spectra WHERE id = "+_id+"");
    def DROP(self):
        self._Connection.ExecuteUpdate("DROP TABLE Spectra");
    def ResultSetIDs(self):
        ids = []
        self._Connection.count = 0
        while self.NextResult():
            ids.append(self.getid())
        return(ids);
    def to_dict(self):
        return({'id' : self.getid(),'Date' : self.getDate(),'No' : self.getNo(),'sCapillary' : self.getsCapillary(),'Membrane' : self.getMembrane(),'MembraneName' : self.getMembraneName(),'Loc2D' : self.getLoc2D(),'Scale2D' : self.getScale2D(),'Area2D' : self.getArea2D(),'Height2D' : self.getHeight2D(),'LocD' : self.getLocD(),'ScaleD' : self.getScaleD(),'AreaD' : self.getAreaD(),'HeightD' : self.getHeightD(),'LocG' : self.getLocG(),'ScaleG' : self.getScaleG(),'AreaG' : self.getAreaG(),'HeightG' : self.getHeightG(),'LocDDp' : self.getLocDDp(),'ScaleDDp' : self.getScaleDDp(),'AreaDDp' : self.getAreaDDp(),'HeightDDp' : self.getHeightDDp(),'AnalysisDate' : self.getAnalysisDate(),'RatioD2D' : self.getRatioD2D(),'RatioD2G' : self.getRatioD2G(),'Ratio2DG' : self.getRatio2DG(),'NoLayers' : self.getNoLayers(),'Comment' : self.getComment(),'SInvestigator' : self.getSInvestigator(),'sSuppressed' : self.getsSuppressed()})
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
        Ret = Ret + " "+ str(self._sCapillary) + ", ";
        Ret = Ret + " "+ str(self._Membrane) + ", ";
        Ret = Ret + " "+ str(self._MembraneName) + ", ";
        Ret = Ret + " "+ str(self._Loc2D) + ", ";
        Ret = Ret + " "+ str(self._Scale2D) + ", ";
        Ret = Ret + " "+ str(self._Area2D) + ", ";
        Ret = Ret + " "+ str(self._Height2D) + ", ";
        Ret = Ret + " "+ str(self._LocD) + ", ";
        Ret = Ret + " "+ str(self._ScaleD) + ", ";
        Ret = Ret + " "+ str(self._AreaD) + ", ";
        Ret = Ret + " "+ str(self._HeightD) + ", ";
        Ret = Ret + " "+ str(self._LocG) + ", ";
        Ret = Ret + " "+ str(self._ScaleG) + ", ";
        Ret = Ret + " "+ str(self._AreaG) + ", ";
        Ret = Ret + " "+ str(self._HeightG) + ", ";
        Ret = Ret + " "+ str(self._LocDDp) + ", ";
        Ret = Ret + " "+ str(self._ScaleDDp) + ", ";
        Ret = Ret + " "+ str(self._AreaDDp) + ", ";
        Ret = Ret + " "+ str(self._HeightDDp) + ", ";
        Ret = Ret + " "+ str(self._AnalysisDate) + ", ";
        Ret = Ret + " "+ str(self._RatioD2D) + ", ";
        Ret = Ret + " "+ str(self._RatioD2G) + ", ";
        Ret = Ret + " "+ str(self._Ratio2DG) + ", ";
        Ret = Ret + " "+ str(self._NoLayers) + ", ";
        Ret = Ret + " "+ str(self._Comment) + ", ";
        Ret = Ret + " "+ str(self._SInvestigator) + ", ";
        Ret = Ret + " "+ str(self._sSuppressed) + ", ";
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
        Ret = Ret + "\"sCapillary\":\"" + self._sCapillary +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Membrane\":\"" + self._Membrane +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"MembraneName\":\"" + self._MembraneName +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Loc2D\":\"" + self._Loc2D +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Scale2D\":\"" + self._Scale2D +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Area2D\":\"" + self._Area2D +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Height2D\":\"" + self._Height2D +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"LocD\":\"" + self._LocD +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ScaleD\":\"" + self._ScaleD +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"AreaD\":\"" + self._AreaD +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"HeightD\":\"" + self._HeightD +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"LocG\":\"" + self._LocG +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ScaleG\":\"" + self._ScaleG +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"AreaG\":\"" + self._AreaG +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"HeightG\":\"" + self._HeightG +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"LocDDp\":\"" + self._LocDDp +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"ScaleDDp\":\"" + self._ScaleDDp +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"AreaDDp\":\"" + self._AreaDDp +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"HeightDDp\":\"" + self._HeightDDp +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"AnalysisDate\":\"" + self._AnalysisDate +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"RatioD2D\":\"" + self._RatioD2D +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"RatioD2G\":\"" + self._RatioD2G +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Ratio2DG\":\"" + self._Ratio2DG +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"NoLayers\":\"" + self._NoLayers +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"Comment\":\"" + self._Comment +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"SInvestigator\":\"" + self._SInvestigator +"\"" ;
        Ret = Ret + ",";
        Ret = Ret + "\"sSuppressed\":\"" + self._sSuppressed +"\"" ;
        if(Bracket == true):
            Ret = Ret + "}";
        return(Ret);
    

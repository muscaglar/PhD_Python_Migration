
import pymysql
from DBSupportLib import *
import json
import os
import inspect

class DBConnection:

    def __init__(self):
        dir = os.path.dirname(os.path.abspath(inspect.stack()[0][1]))
        json_data=open(dir + '/ExptsDB_Settings.json').read()
        settings = json.loads(json_data)
        self.username = settings['Username']
        self.password = settings['Password']
        self.Database = settings['Database']
        self.Hostname = settings['Hostname']

    def OpenConnection(self):
        self.db = pymysql.connect(host = self.Hostname,    # your host, usually localhost
                            user = self.username,         # your username
                            passwd = self.password,  # your password
                            db = self.Database,
                            port = 3306)        # name of the data base
        # you must create a Cursor object. It will let
        #  you execute all the queries you need
        self.cur = self.db.cursor()

    def CloseConnection(self):
        self.db.close()

    def ExecuteUpdate(self, query):
        self.OpenConnection();
        # Use all the SQL you like
        self.cur.execute(query)
        self.CloseConnection()
        return(0)

    def ExecuteQuery(self, query):
        self.OpenConnection();
        # Use all the SQL you like
        self.cur.execute(query)
        self.row = None
        return(0)

    def NextResult(self):
        # print all the first cell of all the rows
        if self.row is None:
            #self.results = self.cur.fetchmany(5)
            self.results = self.cur.fetchall()
            #self.row = self.cur.fetchone();
            if len(self.results) > 0:
                self.row = self.results[0]
                self.count = 1;
            else:
                return(False)
        else:
            if self.count < len(self.results):
                self.row = self.results[self.count]
                self.count += 1;
            else:
                self.row = None
                self.CloseConnection();

        if self.row is not None:
            return (True)
        else:
            self.count = 0;
            return(False)
        #for row in self.cur.fetchall():
            #print row[1]

    def getInt(self, Field):
        return(self.row[Field]);

    def getString(self, Field):
        return(self.row[Field]);

    def getDBDateTime(self, Field):
        return(DBDateTime(self.row[Field]));

    def getTimestamp(self, Field):
        return(DBDateTime(self.row[Field]));

    def getDBDate(self, Field):
        return(DBDate(self.row[Field]));
    def getDate(self, Field):
        return(DBDate(self.row[Field]));

    def getDBTime(self, Field):
        return(DBTime(self.row[Field]));

    def getDouble(self, Field):
        return(self.row[Field]);

    def getFloat(self, Field):
        return(self.row[Field]);

    def getGeog(self, Field):
        return(Geog(self.row[Field],self.row[Field+1]));

    def getAddress(self, Field):
        return(Address(self.row[Field]));

import datetime as dt
import time

class Geog:
    def __init__(self, lat, lon):
        self.lat = lat;
        self.lon = lon;
    def __str__(self):
        #Return a pretty format of the date represented here
        return('Lat ' + str(self.lat) + ' Lon: ' + str(self.lon))

class Address:
    def __init__(self, Addr):
        self.Addr = Addr
    def __str__(self):
        #Return a pretty format of the date represented here
        return(str(self.Addr))

class DBDateTime:
    def __init__ (self, Date = None):
        if Date != None:
            d = dt.datetime.strptime(Date, '%Y-%m-%d %H:%M:%S')    # in java yyyy-MM-dd HH:mm:ss.SSS
            self.dateValue = d

    def __str__(self):
        #Return a pretty format of the date represented here
        return(self.dateValue.strftime('%Y-%m-%d %H:%M:%S'))     # in java yyyy-MM-dd HH:mm:ss.SSS

    def to_datetime(self):
        #Need to deal with issue in windoes where pyton cannot handle negative timestamps
        #https://stackoverflow.com/questions/22082103/on-windows-how-to-convert-a-timestamps-before-1970-into-something-manageable
        #return(dt.datetime.fromtimestamp(self.dateValue / 1e3))
        return(self.dateValue)

    def toLong(self):
        l = time.mktime(dt.timetuple())
        return(l)

    def before(self, d):
        if d.toLong() > self.toLong():
            return(True)
        return(False)

    def after(self, d):
        if d.toLong() < self.toLong():
            return(True)
        return(False)

class DBDate(DBDateTime):
    def __init__(self, Date = None):
        if Date != None:
            d = dt.datetime.strptime(Date, '%Y-%m-%d')
            self.dateValue = d
    def __str__(self):
        #Return a pretty format of the date represented here
        return(self.dateValue.strftime('%Y-%m-%d'))

class DBTime(DBDateTime):
    def __init__(self, Date = None):
        if Date != None:
            d = dt.datetime.strptime(Date, '%H:%M:%S')
            self.dateValue = d

    def __str__(self):
        #Return a pretty format of the date represented here
        return(self.dateValue.strftime('%H:%M:%S'))

#class File:
#    def __init__(self, Addr):
#        self.Addr = Addr
#    def __str__(self):
#        #Return a pretty format of the date represented here
#        return(str(self.Addr))
#
#class Image:
#    def __init__(self, Img):
#        self.Image = Img
#    def __str__(self):
#        #Return a pretty format of the date represented here
#        return(str(self.Image))

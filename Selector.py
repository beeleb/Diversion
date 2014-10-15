#coding: utf-8
import csv   #csvモジュールをインポートする
import random

class Kuji:
    def __init__(self):
        self.list = []
    def first_start(self):
        f = open('namelist.csv', 'r')
        dataReader = csv.reader(f)
        self.list = []
        for row in dataReader:
            for p in row:
                self.list.append(p)
        print "ｻｲｼｮｶﾗ ﾊｼﾞﾒﾏｽ"
        print self.list
    

    def restart(self):
        g = open('currentname.csv', 'r')
        dataReader2 = csv.reader(g)
        self.list = []
        for row in dataReader2:
            for p in row:
                self.list.append(p)
        print "ｷｮｳﾊ ｺｺｶﾗ ﾊｼﾞﾒﾏｽ"
        print self.list

    def choice(self):
        
        c = random.choice(self.list)
        self.list.remove(c)
        print "ﾂｷﾞﾊ ｱﾅﾀﾃﾞｽ, "+c+"ｻﾝ"
        if self.list ==[]:
            print "ｾﾞﾝｲﾝ ﾂｶｲｷｯﾀﾉﾃﾞ ﾂｷﾞﾉｼｭｳｦ ﾊｼﾞﾒﾏｽ"
            f = open('namelist.csv', 'r')
            dataReader = csv.reader(f)
            for row in dataReader:
                for p in row:
                    self.list.append(p)
        else:
            print "ﾏﾀﾞ ﾉｺｯﾃｲﾙﾉﾊ ｲｶﾉ ﾋﾄﾀﾁﾃﾞｽ"
            print self.list
    
    def finish(self):
        print "ｷｮｳﾊ ｺﾚﾃﾞ ｵﾜﾘﾏｽ, ｲｶﾉ ﾘｽﾄｦ ﾎｿﾞﾝｼﾏｼﾀ"
        print self.list
        h = open('currentname.csv', 'w')
        csvWriter = csv.writer(h)
        csvWriter.writerow(self.list)

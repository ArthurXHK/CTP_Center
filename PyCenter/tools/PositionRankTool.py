# -*- coding: utf-8 -*-
import zipfile
import os.path
import os
import pymongo
import re
from datetime import datetime
import time
'''
#extract all zip file
zippath = 'C:\\Users\\Administrator\\Desktop\\333333\\'
zipfiles = os.listdir(zippath)


for file in zipfiles:
    print file
    zfile = zipfile.ZipFile(zippath + file)
    filename = file.split('.')[0]
    if os.path.exists(zippath + filename):
        os.mkdir(zippath + filename)
    zfile.extractall(zippath + filename)
    
'''


'''
#insert data
conn = pymongo.MongoClient('198.16.100.11')
db = conn.position
path = u'C:/Users/Administrator/Desktop/333333/'
folders = os.listdir(path)


for folder in folders:
    print folder
    files = os.listdir(path + folder + '/')
    for file in files:
        
        filedata = open(path + folder + '/' + file, 'r')
        instdateinfo = file.split('_')
        date = instdateinfo[0]
        date = datetime(int(date[0:4]), int(date[4:6]), int(date[6:8]))
        inst = instdateinfo[1]
        line = filedata.readline()
        while line:
            ss = re.split('\s+', line)
            
            if len(ss) > 4:
                if ss[2] == u'成交量':
                    type = 'volume'
                elif ss[2] == u'持买单量':
                    type = 'bid'
                elif ss[2] == u'持卖单量':
                    type = 'ask'
                elif ss[0] != '':
                    #print file
                    #print line.encode('utf-8')
                    #print ss
                    db.PositionRank.insert({'instrument': inst, 'date': date, 'type': type, 'rank': int(ss[0]),
                                        'user': ss[1].encode('utf-8'), 'value': int(ss[2]), 'diff': int(ss[3])})
            line = filedata.readline()
'''


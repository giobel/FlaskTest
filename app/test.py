import os
import collections
import csv
from collections import defaultdict
import mysql.connector
from mysql.connector import errorcode

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'images/')

image_names = os.listdir(target)


def get_csv():
    csv_path = './static/projectDrg.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

d = get_csv()
keys = []
dt = []
items = []
values = []

for item in d:
    items.append(item)
    subVal = []
    values.append(subVal)
    for k, v in item.items():
        keys.append(k)
        subVal.append(v)

t = [list(x) for x in zip(*values)]


def get_dict():
    csv_path = './static/projectDrg.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    return csv_obj


dic = get_dict()

sheetByRevision = {}

revisions = []
sheets = []

for s in dic:
        revisions.append(s['Rev4'])
        sheets.append(s['Drg_No'])


sheetByRevision = dict(zip(sheets,revisions))



v = defaultdict(list)

for key, value in sorted(sheetByRevision.items()):
    v[value].append(key)


def massageCsv(filePath):
        csv_path = filePath
        csv_file = open(csv_path, 'r')
        csv_obj = csv.DictReader(csv_file)
        revisions = []
        sheets = []
        for s in csv_obj:
                revisions.append(s['Rev4'])
                sheets.append(s['Drg_No'])
        sheetByRevision = dict(zip(sheets, revisions))
        output = defaultdict(list)
        for key, value in sorted(sheetByRevision.items()):
                output[value].append(key)
        return output

vi = massageCsv('./static/projectDrg.csv')

for k in vi:
        #print (k)
        for v in k:
                for sheet in vi[k]:
                        continue
                        #print (sheet)

sheets = [{"Revision A":["105", "100", "106"]},{"Revision B":["230", "260", "261"]},{"Revision C":["310","311","312"]}]

keys = ['a','b','c']

sh = [['105','106'],['201','202'],['301','350']]

dictionar = {}

for i in range(0,len(keys)):
        for j in range(0,len(sh[i])):
                dictionar.setdefault(keys[i],[]).append(sh[i][j])

def massageCsvRevisited(filePath):
        reader = csv.reader(open(filePath))
        trans = list(map(list, zip(*reader)))
        d={}
        for row in trans:
                d[row[0]]=row[1:]
        return d

#walls = massageCsvRevisited('./static/structuralFramings.csv')


def parseTxt(filePath):
        f = open(filePath,'r')
        rows = []
        text = f.readlines()
        for t in text:
                t.split(',')
                rows.append(t)
        return rows

#rows = massageCsvRevisited('./static/Structural Framing Schedule.csv')

rows = massageCsvRevisited('./static/wall.csv')
keys = [*rows.keys()]
rowsCount = len(rows[keys[0]])
"""
for i in range(0,rowsCount):
         for w in rows.values():
                print(w[i])
"""


cnx = mysql.connector.connect(user='root', password='', host='127.0.0.1', database='swc_asl')
cursor = cnx.cursor()
"""
query = ("SELECT * FROM `structuralframing` WHERE `Length` >= '10.0'")

cursor.execute(query)

result = []
for a in cursor:
  result.append(a)

print([r for r in result])
"""

columns = ("SELECT * FROM `structuralframing` WHERE `Length` >= '10.0'")


def getTableColumnNames(cnx, tableName):
        cursor = cnx.cursor()
        cursor.execute('SHOW COLUMNS FROM ' + tableName)
        return [c[0] for c in cursor]

names = getTableColumnNames(cnx, 'structuralframing')


def getTableValues(cnx, tableName):
        cursor = cnx.cursor()
        query = ("SELECT * FROM " + tableName)
        cursor.execute(query)
        return [c for c in cursor]




tv = getTableValues(cnx, 'structuralframing')

for t in tv:
        for i in t:
                print (i)



"""
columns = defaultdict(list) # each value in each column is appended to a list

values = walls.values()
keys = walls.keys()

for i in range(0,len(keys)):
        for w in values:
                print (w[i])

content = os.listdir(APP_ROOT+'\static')

images = []
for c in content: 
        if 'png' in c:
                name = c.split(' ')
                try:
                        images.append(name[4])
                except:
                        continue

print(images)
"""
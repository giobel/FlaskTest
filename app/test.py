import os
import collections
import csv
from collections import defaultdict

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'images/')

image_names = os.listdir(target)


def get_csv():
    csv_path = './static/la-riots-deaths.csv'
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

for rev in items:
        print (rev)


sheets = [{"Revision A":["105", "100", "106"]},{"Revision B":["230", "260", "261"]},{"Revision C":["310","311","312"]}]

keys = ['a','b','c']

sh = [['105','106'],['201','202'],['301','350']]

dictionar = {}

for i in range(0,len(keys)):
        for j in range(0,len(sh[i])):
                dictionar.setdefault(keys[i],[]).append(sh[i][j])

print(vi)
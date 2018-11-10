import os
from datetime import datetime
import re
import csv
from collections import defaultdict


def get_csv():
    csv_path = './static/projectDrg.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list


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

def csvHeaders(filePath):
        reader = csv.reader(open(filePath))
        trans = list(map(list, zip(*reader)))
        return [t[0] for t in trans]

def csvRows(filePath):
        return csv.reader(open(filePath))

def massageCsvRevisited(filePath):
        reader = csv.reader(open(filePath))
        trans = list(map(list, zip(*reader)))
        d={}
        for row in trans:
                d[row[0]]=row[1:]
        return d
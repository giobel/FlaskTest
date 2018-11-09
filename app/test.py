import os
import collections
import csv

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

for obj in d:
    print(obj.full_name)

import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

target = os.path.join(APP_ROOT, 'images/')

image_names = os.listdir(target)

print (image_names[0][41:44])
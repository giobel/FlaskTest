from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os
from datetime import datetime
import re
import csv
from collections import defaultdict
import helpers

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sheets')
def sheets():
    formatted_now = datetime.now().strftime("%d/%m/%y")
    items = helpers.massageCsv('./static/projectDrg.csv')
    return render_template('sheets.html', items = items, date = formatted_now)

@app.route('/model')
def model():
    return render_template('world.html')

@app.route("/gallery")
def getGallery():
    image_names = os.listdir('./images')
    return render_template("gallery.html", imageNames = image_names)

@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images", filename)

@app.route("/drawingRegister")
def drawingRegister():
    object_list = helpers.get_csv()
    return render_template('drawingRegister.html', object_list=object_list)

@app.route('/elements')
def elements():
    rows = helpers.massageCsvRevisited('./static/wall.csv')
    keysCount = len(rows.keys())
    return render_template('elements.html', rows = rows, keysCount = keysCount, title = "Wall Schedule")

if __name__ == "__main__":
    app.run()
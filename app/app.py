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

@app.route('/walls')
def walls():
    rows = helpers.massageCsvRevisited('./static/wall.csv')
    keys = [*rows.keys()]
    keysCount = len(rows[keys[0]])
    return render_template('walls.html', rows = rows, keysCount = keysCount, title = "Wall Schedule")

@app.route('/structuralFramings')
def structuralFramings():
    rows = helpers.massageCsvRevisited('./static/Structural Framing Schedule.csv')
    keys = [*rows.keys()]
    rowsCount = len(rows[keys[0]])
    return render_template('structuralFramings.html', rows = rows, rowsCount = rowsCount, title = "Structural Framings Schedule")

@app.route('/elementSchedule')
def elementSchedule():
    return render_template('elementSchedule.html', title = "Element Schedule")

@app.route('/instances')
def instances():
    cnx = helpers.connectDB('swc_asl')
    tableName = 'walls'
    tableHeaders = helpers.getTableColumnNames(cnx, tableName)
    tableValues = helpers.getTableValues(cnx, tableName)
    return render_template('instances.html', tableHeaders = tableHeaders, tableValues = tableValues)


if __name__ == "__main__":
    app.run()
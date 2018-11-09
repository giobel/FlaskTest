from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os
from datetime import datetime
import re
import csv


app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sheets')
def sheets():
    formatted_now = datetime.now().strftime("%d/%m/%y")
    object_list = get_csv()
    sheets = [{"Revision A":["105", "100", "106"]},{"Revision B":["230", "260", "261"]},{"Revision C":["310","311","312"]}]
    image_names = os.listdir('./images')
    return render_template('sheets.html', sheets = sheets, date = formatted_now, imageNames = image_names)

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

def get_csv():
    csv_path = './static/projectDrg.csv'
    csv_file = open(csv_path, 'r')
    csv_obj = csv.DictReader(csv_file)
    csv_list = list(csv_obj)
    return csv_list

@app.route("/drawingRegister")
def drawingRegister():
    object_list = get_csv()
    return render_template('drawingRegister.html', object_list=object_list)


if __name__ == "__main__":
    app.run()
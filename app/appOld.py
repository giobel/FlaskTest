from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os
from datetime import datetime
import re

app = Flask(__name__)

APP_ROOT = os.path.dirname(os.path.abspath(__file__))

@app.route("/")
def index():
    return render_template('upload.html')

@app.route("/upload", methods = ['POST'])
def upload():
    target = os.path.join(APP_ROOT, 'images/')
    for f in request.files.getlist("file"):
        filename = f.filename
    return render_template("gallery.html", image_name = filename)

@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images", filename)


@app.route("/gallery")
def getGallery():
    image_names = os.listdir('./images')
    return render_template("gallery.html", imageNames = image_names, imageNumbers = "ciao")


@app.route('/<name>')
def hello(name):
    now = datetime.now()
    formatted_now = now.strftime("%A, %d %B, %Y at %X")
    content = "<strong>Hello there, " + name + "!</strong> It's " + formatted_now
    return render_template('hello.html',title = "Hello flusk", contento = content, date = now, name = name)

@app.route("/api/data")
def get_data():
    return app.send_static_file("data.json")

@app.route("/sheets")
def sheets():
    sheets = [{"Revision A":["105", "110", "120"]},{"Revision B":["200", "201", "230"]},{"Revision C":["300","320","340"]}]
    return render_template("home.html", sheets = sheets)

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")



if __name__ == "__main__":
    app.run()

"""
@app.route("/sheets/")
def sheets():
    APP_ROOT = os.path.dirname(os.path.abspath(__file__))
    target = os.path.join(APP_ROOT, 'images/')
    image_names = os.listdir(target)
    return render_template("gallery.html", image_name = image_names[0])

"""

# env\scripts\activate activate the environment 
# flask run



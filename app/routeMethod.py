from flask import Flask, flash, redirect, render_template, request, send_from_directory
import os
from datetime import datetime
import re

app = Flask(__name__)



@app.route("/gallery")
def getGallery():
    image_names = os.listdir('./images')
    return render_template("gallery.html", imageNames = image_names, imageNumbers = "ciao")


@app.route("/upload/<filename>")
def send_image(filename):
    return send_from_directory("images", filename)



if __name__ == "__main__":
    app.run()
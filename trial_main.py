# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:22:06 2021

@author: Abhinav Raj
"""

import pandas as pd
import os

from examtimetable import ExamTimeTable

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

time_table = ExamTimeTable()

UPLOAD_FOLDER = os.path.join(os.getcwd(),'data')
ALLOWED_EXTENSIONS = {'txt'}

app = Flask(__name__)
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 3

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS



# @app.route('/upload_data')
# def upload():
#     return render_template('upload_data.html')
@app.route('/')
def home():
    return render_template('home.html')

@app.route('/products')
def products():
    return render_template('products.html')

# @app.route('/upload_data')
# def upload_data():
#     return render_template('upload_data.html')

@app.route('/upload_data',methods = ['GET','POST'])
def upload_data():
    if request.method == 'POST':
        image_file = request.files['image']
        if image_file:
            image_location = os.path.join(UPLOAD_FOLDER,image_file.filename)
            image_file.save(image_location)
            time_table(pd.read_csv(image_location),image_file.filename)
            try:
                os.remove(image_location)
            except Exception as exc:
                pass
            return render_template('class_network.html')
    return render_template('upload_data.html')

@app.route('/class_network')
def class_network():
    return render_template('class_network.html')
@app.route('/bipartite')
def bipartite():
    return render_template('bipartite.html')
@app.route('/projected')
def projected():
    return render_template('projected.html')

if __name__ == "__main__":
    app.run(debug=True)
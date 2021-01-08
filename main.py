# -*- coding: utf-8 -*-
"""
Created on Wed Jan  6 12:22:06 2021

@author: Abhinav Raj
"""

import pandas as pd

from examtimetable import ExamTimeTable

from flask import Flask, flash, request, redirect, url_for, render_template
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = '/path/to/the/uploads'
ALLOWED_EXTENSIONS = {'txt'}



data = pd.read_csv('cms_data.txt',header = None)

time_table = ExamTimeTable()

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/')
def home():
    return render_template('upload_data.html')

@app.route('/products')
def products():
    return render_template('products.html')

@app.route('/class_network')
def class_network():
    return render_template('class_network.html')
@app.route('/bipartite')
def bipartite():
    return render_template('bipartite.html')
@app.route('/projected')
def projected():
    return render_template('projected.html')

def example():
    return time_table(data)

# if __name__ == '__main__':
#     example()
if __name__ == "__main__":
    app.run(debug=True)

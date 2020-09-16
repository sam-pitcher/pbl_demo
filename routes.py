from flask import render_template, request
# from app import app_object, pbl

import json
from main import app
import pbl

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', title='Homepage')

@app.route('/voc', methods=['GET', 'POST'])
def voc():
    url = pbl.generate()
    print(url)
    return render_template('voc.html', url=url)
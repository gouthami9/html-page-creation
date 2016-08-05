from flask import render_template
from webpage2 import app

@app.route('/')
def index():
    return render_template('layout1.html')
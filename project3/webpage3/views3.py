from flask import render_template
from webpage3 import app

@app.route('/')
def index():
    return render_template('layout3.html')
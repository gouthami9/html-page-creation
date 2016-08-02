from flask import render_template
from webpage import app

@app.route('/')
def index():
    return render_template('layout.html')
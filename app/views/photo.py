__author__ = 'jorge'
from app import app
from flask import render_template


@app.route('/importphoto')
def import_photo():

    return render_template('photo/importPhoto.html')


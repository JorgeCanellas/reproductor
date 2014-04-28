__author__ = 'jorge'
from app import app
from flask import render_template


@app.route('/films')
def film():
    return render_template("films.html")


@app.route('/importfilm')
def import_film():
    return render_template("importFilm.html")



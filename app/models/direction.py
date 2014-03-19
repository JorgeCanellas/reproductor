__author__ = 'jorge'
from sqlalchemy import Column
from app import db

direction = db.Table('direction',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('director_id', db.Integer, db.ForeignKey('Director.id'))
)
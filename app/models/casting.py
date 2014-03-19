__author__ = 'jorge'

from sqlalchemy import Column
from app import db


casting = db.Table('casting',
    Column('film_id', db.Integer, db.ForeignKey('Film.id')),
    Column('actor_id', db.Integer, db.ForeignKey('Actor.id'))
)
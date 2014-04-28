__author__ = 'jorge'

from app import db
from sqlalchemy import Column

photo_album = db.Table('photo_album',
                      Column('photo_id', db.Integer, db.ForeignKey('Photo.id')),
                      Column('album_id', db.Integer, db.ForeignKey('Album.id')))
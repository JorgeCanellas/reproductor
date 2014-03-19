__author__ = 'jorge'

from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy.orm import relationship
from app.models import photoAlbum
from app import db


class Photo(db.Model):
    __tablename__ = "photo"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    date = Column(DateTime)
    link = Column(String(120))
    album = relationship("Album", secondary=photoAlbum)

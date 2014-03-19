__author__ = 'jorge'

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from app.models import photoAlbum
from app import db


class Album(db.Model):
    __tablename__ = "album"
    id = Column(Integer, primary_key=True)
    name = Column(String(120))
    photos = relationship("Photo", secondary=photoAlbum)

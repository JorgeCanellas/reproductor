__author__ = 'jorge'
from sqlalchemy import Column, Integer, String
from app import db


class Genre(db.Model):
    __tablename__ = "genres"
    id = Column(Integer, primary_key=True)
    name = Column(String(120), unique=True)

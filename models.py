from sqlalchemy import Column, ForeignKey, Integer
from sqlalchemy.orm import relationship
from sqlalchemy_imageattach.entity import Image, image_attachment
from database import db


class Users(db.Model):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(9))
    # picture = image_attachment('UserPicture')

    def __repr__(self):
        return '<User %r>' % self.name


# class UsersPicture(db.Model, Image):
#     __tablename__ = 'user_picture'
#     user_id = Column(Integer, ForeignKey('user.id'), primary_key=True)
#     user = relationship('User')




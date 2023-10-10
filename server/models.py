from flask_sqlalchemy import SQLAlchemy
from sqlalchemy_serializer import SerializerMixin
from sqlalchemy.orm import validates

db = SQLAlchemy()


class User(db.Model, SerializerMixin):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String, nullable=False)
    last_name = db.Column(db.String, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)
    doghouses = db.relationship('Review', back_populates='user')
    


class DogHouse(db.Model, SerializerMixin):
    __tablename__ = 'doghouse'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False) 
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    image = db.Column(db.String(250), nullable=False)
    description = db.Column(db.String(), nullable=False)
    users = db.relationship('Review', back_populates='doghouse')
    

class Review(db.Model, SerializerMixin):
    __tablename__ = 'review'
    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String, nullable=False)
    rating = db.Column(db.Integer, nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    doghouse_id = db.Column(db.Integer, db.ForeignKey('doghouse.id'), nullable=False)
    user = db.relationship('User', back_populates='doghouses')
    doghouse = db.relationship('DogHouse', back_populates='users')
   

    @validates('email', 'password')
    def validate_email_and_password(self, key, email,password):
        if key == 'email':
            if not email:
                raise AssertionError('Invalid email')
           
        
        if key == 'password':
            if not password:
                raise AssertionError('Invalid Password')
            

        return email, password

    
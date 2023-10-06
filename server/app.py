import os
from flask import Flask, jsonify, make_response, request
from flask_migrate import Migrate
from flask_restful import Api, Resource
from models import db, User, DogHouse, Review

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URI')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

migrate = Migrate(app, db)


@app.route('/')
def home():
    return 'Welcome to the Dog House'
           

@app.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    email = data.get('email')
    password = data.get('password')
    
    new_user = User(email=email, password=password)
    db.session.add(new_user)
    db.session.commit()
    
    return jsonify(message='User created successfully!'), 201

@app.route('/doghouses', methods=['POST'])
def create_doghouse():
    data = request.get_json()
    name = data.get('name')
    latitude = data.get('latitude')
    longitude = data.get('longitude')
    user_id = data.get('user_id')
    
    user = User.query.get(user_id)
    if user is None:
        return jsonify(error='User not found'), 404
    
    new_doghouse = DogHouse(name=name, location=location, user_id=user_id)
    db.session.add(new_doghouse)
    db.session.commit()
    
    return jsonify(message='Dog house created successfully!'), 201

@app.route('/reviews', methods=['POST'])
def create_review():
    data = request.get_json()
    content = data.get('content')
    rating = data.get('rating')
    user_id = data.get('user_id')
    doghouse_id = data.get('doghouse_id')
    
    user = User.query.get(user_id)
    doghouse = DogHouse.query.get(doghouse_id)
    
    if user is None or doghouse is None:
        return jsonify(error='User or dog house not found'), 404
    
    new_review = Review(content=content, rating=rating, user_id=user_id, doghouse_id=doghouse_id)
    db.session.add(new_review)
    db.session.commit()
    
    return jsonify(message='Review created successfully!'), 201

@app.route('/users', methods=['GET'])
def get_users():
    users = User.query.all()
    users_list = []
    for user in users:
        users_list.append({
            'id': user.id,
            'email': user.email
        })
    return jsonify(users_list)

@app.route('/doghouses', methods=['GET'])
def get_doghouses():
    doghouses = DogHouse.query.all()
    doghouses_list = []
    for doghouse in doghouses:
        doghouses_list.append({
            'id': doghouse.id,
            'name': doghouse.name,
            'latitude': doghouse.latitude,
            'longitude': doghouse.longitude,
            'image': doghouse.image,
            'description':doghouse.description
            
        })
    return jsonify(doghouses_list)

@app.route('/reviews', methods=['GET'])
def get_reviews():
    reviews = Review.query.all()
    reviews_list = []
    for review in reviews:
        reviews_list.append({
            'id': review.id,
            'content': review.content,
            'rating': review.rating,
            'user_id': review.user_id,
            'doghouse_id': review.doghouse_id
        })
    return jsonify(reviews_list)

with app.app_context():
        db.create_all()

if __name__ == '__main__':
    app.run(debug=True)

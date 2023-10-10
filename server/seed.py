from random import randint, choice as rc

from faker import Faker

from app import app

from models import db, User, DogHouse, Review

fake = Faker()

dog_house_name = [
    "Crazy Dog Kennel",
    "Pup With Me",
    "Joyful Puppies",
    "Dog Playground",
    "Kind Care Kennel",
    "Jetsetters Pet Lodge",
    "Place Kennels",
    "pool read Kennel",
    "Smooch Pooch",
    "VCA Mountain Kennel",
    "House Pet Paradise",
    "A Dog Gone Wild",
    "Puppy Kingdom Kennel",
    "The Gold Digger Kennels",
    "final Pet Utopia",
    "Cavorting Canines",
    "The good alternative",
    "Hills Dog Boarding",
    "massive Paw Dog Kennel",
    "No a lot of Kennels",
    "Barking Shed",
    "The cur Hut"
]

dog_house_image = [
    "https://i.pinimg.com/564x/57/41/3c/57413ce0f04d56b8028f6b2e8ea461fa.jpg",
    "https://i.pinimg.com/564x/6c/68/25/6c68251565197366a06fc167095761b1.jpg",
    "https://i.pinimg.com/236x/70/60/a6/7060a6f7c765aa96a195444a18e54ba4.jpg",
    "https://i.pinimg.com/236x/78/6f/ab/786fab40b4cbe1c64b193065add56072.jpg",
    "https://i.pinimg.com/236x/f1/e7/4d/f1e74d022711c0edab9eb6da421ce334.jpg",
    "https://i.pinimg.com/236x/e2/8e/6c/e28e6c8b4cfdea8e1fb22c772004f91b.jpg",
    "https://i.pinimg.com/236x/5e/4e/3b/5e4e3bd3f269c8578718ce2c3f04c507.jpg",
    "https://i.pinimg.com/236x/58/43/a8/5843a80092afb29e836e3e25d0c7e5e7.jpg",
    "https://i.pinimg.com/236x/1d/30/52/1d305248406bc15aab1aea0900011770.jpg",
    "https://i.pinimg.com/236x/5c/f3/f3/5cf3f3ea617af0a4d6a98e2465b8db49.jpg",
    "https://i.pinimg.com/236x/12/72/a1/1272a1872eeb942d1838e350d4a2fdb9.jpg",
    "https://i.pinimg.com/236x/18/a6/0a/18a60a51fbe1989e9b066d0469c3935d.jpg",
    "https://i.pinimg.com/236x/49/01/c5/4901c56571ddb21c33db3a61e671069c.jpg",
    "https://i.pinimg.com/236x/7a/ca/86/7aca86878567046297ae3933ac63a6b4.jpg",
    "https://i.pinimg.com/236x/1c/b7/9b/1cb79bd774a425e6b096f68a96c5b0e6.jpg",
    "https://i.pinimg.com/236x/d9/f2/e0/d9f2e02b8f4b067f6dd4a17d8820c7d0.jpg",
    "https://i.pinimg.com/236x/60/4e/d2/604ed289b041b624325e673f7bbb8731.jpg",
    "https://i.pinimg.com/236x/23/9b/4d/239b4dd8637075d39fe2e61b046d654e.jpg",
    "https://i.pinimg.com/236x/a4/18/49/a4184979145ccabca327d31d182a4542.jpg",
    "https://i.pinimg.com/236x/6e/88/fd/6e88fd8eb24628bd7cbb26e9deaa52c2.jpg",
    "https://i.pinimg.com/236x/ee/64/5f/ee645f6010cf1766e3e7268def4256e3.jpg",
]


with app.app_context():
    
    User.query.delete()
    DogHouse.query.delete()
    Review.query.delete()

    # seeding users
    users = []
    for i in range(10):
        u = User(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            email=fake.email(),
            password = fake.password(),
            # location
            )
        users.append(u)

    db.session.add_all(users)
    db.session.commit()

    # seeding dog houses
    dog_houses = []
    for i in range(20):
        d = DogHouse(
            name=rc(dog_house_name),
            image=rc(dog_house_image),
            description = fake.sentence(),
            latitude = fake.latitude(),
            longitude = fake.longitude()
            
            # price_per_night = randint(5,15)
        )
        dog_houses.append(d)

    db.session.add_all(dog_houses)
    db.session.commit()

    # Adding reviews
    all_users = User.query.all()
    all_dog_houses = DogHouse.query.all()

    for user in all_users:
        rating = randint(1,5)
        content = fake.sentence()
        dogHouse = rc(all_dog_houses)
        r = Review(user_id=user.id, doghouse_id=dogHouse.id, content=content, rating=rating)
        db.session.add(r)

    db.session.commit()

from sqlalchemy import create_engine
from pymongo.mongo_client import MongoClient
from sqlalchemy.orm import sessionmaker
from models import base, User

uri = "mongodb+srv://admin:47ezDKGiJ5xiHJQF@hack-ku.uwg8jse.mongodb.net/?retryWrites=true&w=majority&appName=Hack-KU"

# Create a new client and connect to the server
client = MongoClient(uri)


events = client["events"]
future_events = client["future_events"]
locations = client["locations"]

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

engine = create_engine('sqlite:///main.db')
session_maker = sessionmaker(bind=engine)
base.metadata.create_all(engine)


def store_event(user: User, location: str, hours: int, description: str, date: str, time: str, affiliation: str = None):
    data = {
        "location": location,
        "hours": hours,
        "datetime": date + " " + time,
        "description": description,
        "affiliation": affiliation
    }
    collection = events[str(user.id)]
    collection.insert_one(data)


def get_events(user: User):
    return events[str(user.id)].find()


def store_location(name: str, address: str, city: str, state: str, zipcode: int):
    data = {
        "name": name,
        "address": address,
        "city": city,
        "state": state,
        "zipcode": zipcode
    }
    collection = locations["locations"]
    collection.insert_one(data)


def get_locations():
    collection = locations["locations"]
    return collection.find()


def store_future_event(user: User, location: str, date: str, time: str, affiliation: str = None):
    data = {
        "location": location,
        "datetime": date + " " + time,
        "affiliation": affiliation
    }
    collection = future_events[str(user.id)]
    collection.insert_one(data)


def get_future_events(user: User):
    return future_events[str(user.id)].find()

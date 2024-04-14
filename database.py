from sqlalchemy import create_engine
from pymongo.mongo_client import MongoClient
from sqlalchemy.orm import sessionmaker
from models import base, User

uri = "mongodb://10.0.0.182"

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
    """
        This function stores an event in the database.

        Args:
            user (User): The user who is creating the event.
            location (str): The location of the event.
            hours (int): The number of hours the event will last.
            description (str): A description of the event.
            date (str): The date of the event.
            time (str): The time of the event.
            affiliation (str, optional): The affiliation of the event, such as a company or organization. Defaults to None.

        Returns:
            None

        """
    data = {
        "location": location,
        "hours": hours,
        "datetime": date + " " + time,  # format is found in config.py
        "description": description,
        "affiliation": affiliation
    }
    collection = events[str(user.id)]
    collection.insert_one(data)


def get_events(user: User):
    return events[str(user.id)].find()


def store_location(user: User, name: str, address: str, city: str, state: str, zipcode: int):
    """
        This function stores a location in the database.

        Args:
            user (User): The user who is creating the location.
            name (str): The name of the location.
            address (str): The address of the location.
            city (str): The city of the location.
            state (str): The state of the location.
            zipcode (int): The zipcode of the location.

        Returns:
            None

        """
    data = {
        "name": name,
        "address": address,
        "city": city,
        "state": state,
        "zipcode": zipcode
    }
   # print("attempting to store location")
   # print(data)
    collection = locations[str(user.id)]
    collection.insert_one(data)


def get_locations(user: User):
    collection = locations["locations"]
    return collection[str(user.id)].find()


def store_future_event(user: User, location: str, date: str, time: str, affiliation: str = None):
    """
        This function stores a future event in the database.

        Args:
            user (User): The user who is creating the future event.
            location (str): The location of the future event.
            date (str): The date of the future event.
            time (str): The time of the future event.
            affiliation (str, optional): The affiliation of the future event, such as a company or organization. Defaults to None.

        Returns:
            None

        """
    data = {
        "location": location,
        "datetime": date + " " + time,
        "affiliation": affiliation
    }
    collection = future_events[str(user.id)]
    collection.insert_one(data)


def get_future_events(user: User):
    return future_events[str(user.id)].find()
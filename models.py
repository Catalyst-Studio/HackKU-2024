from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


# a class that represents a user in the database
class User(base):
    """
        This class represents a user in the database.

        Parameters:
            id (int): The user's unique ID.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            password (str): The user's password.

        Attributes:
            id (int): The user's unique ID.
            first_name (str): The user's first name.
            last_name (str): The user's last name.
            email (str): The user's email address.
            password (str): The user's password.
        """
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)
    email = Column(String)
    password = Column(String)

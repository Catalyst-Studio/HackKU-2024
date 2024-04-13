from datetime import timedelta

from fastapi import FastAPI
from fastapi_login import LoginManager

import database
from database import session_maker

from models import User


async def get_user(email):
    """
        Get a user by their email address.

        Args:
            email (str): The email address of the user.

        Returns:
            Optional[User]: The user with the matching email address, or None if no user was found.
        """
    session = session_maker()
    user = session.query(User).filter_by(email=email).first()
    return user


secret = "sldkfjbgnksdrgyh8q3ghisdfgbweriytug"
manager = LoginManager(secret, "/login", cookie_name="auth-key", use_cookie=True, use_header=False, default_expiry=timedelta(hours=12))


@manager.user_loader()
async def load_user(user_email: str):
    return await get_user(user_email)


def make_user(first_name, last_name, email, password):
    """
        Creates a new user in the database.

        Args:
            first_name (str): The first name of the user.
            last_name (str): The last name of the user.
            email (str): The email address of the user.
            password (str): The password of the user.

        Returns:
            User: The newly created user.
        """
    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    session = session_maker()
    session.add(user)
    session.commit()
    session.close()
    return user


def verify_user(email, password):
    """
        Verify a user's login credentials.

        Args:
            email (str): The email address of the user.
            password (str): The password of the user.

        Returns:
            bool: True if the credentials are valid, False otherwise.
        """
    session = session_maker()
    user = session.query(User).filter_by(email=email).first()
    if user is not None:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False

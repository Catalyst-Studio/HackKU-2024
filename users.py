from datetime import timedelta

from fastapi import FastAPI
from fastapi_login import LoginManager

import database
from database import session_maker

from models import User


async def get_user(email):
    session = session_maker()
    user = session.query(User).filter_by(email=email).first()
    return user


secret = "sldkfjbgnksdrgyh8q3ghisdfgbweriytug"
manager = LoginManager(secret, "/login", cookie_name="auth-key", use_cookie=True, use_header=False, default_expiry=timedelta(hours=12))


@manager.user_loader()
async def load_user(user_email: str):
    return await get_user(user_email)


def make_user(first_name, last_name, email, password):
    user = User(first_name=first_name, last_name=last_name, email=email, password=password)
    session = session_maker()
    session.add(user)
    session.commit()
    session.close()
    return user


def verify_user(email, password):
    session = session_maker()
    user = session.query(User).filter_by(email=email).first()
    if user is not None:
        if user.password == password:
            return True
        else:
            return False
    else:
        return False

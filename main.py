from urllib import request

from fastapi import FastAPI, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from starlette.responses import RedirectResponse

import api_util
import database
import users
import api

# Making the initial app
app = FastAPI()
app.include_router(api.api_router)
# Adding all the statis files to the webserver
app.mount("/static", StaticFiles(directory="static"), name="static")
# Making the templating engine
templates = Jinja2Templates("templates")


# Rendering Pages
@app.get("/")
async def index(request: Request):
    return RedirectResponse("/login")


@app.get("/home")
async def home(request: Request, user=Depends(users.manager)):
    events = database.get_events(user)
    return templates.TemplateResponse("view-events.html", {"request": request, "events": events})


@app.get("/add-event")
async def add_event(request: Request, user=Depends(users.manager)):
    return templates.TemplateResponse("add-event.html", {"request": request, "locations": database.get_locations(user)})


@app.get("/export-event")
async def export_event(request: Request, user=Depends(users.manager)):
    return templates.TemplateResponse("export-event.html", {"request": request})


@app.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup")
async def signup_user(request: Request, first_name=Form(), last_name=Form(), email=Form(), password=Form()):
    """
    This function creates a new user in the system.

    Args:
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
        email (str): The email of the user.
        password (str): The password of the user.

    Returns:
        starlette.responses.RedirectResponse: A redirect response to the home page.
    """
    users.make_user(first_name, last_name, email, password)
    token = users.manager.create_access_token(data=dict(sub=email))
    response = RedirectResponse("/home", status_code=302)
    users.manager.set_cookie(response, token)
    return response


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_user(request: Request, email=Form(), password=Form()):
    """
        This function authenticates a user using their email and password.

        Args:
            email (str): The email of the user.
            password (str): The password of the user.

        Returns:
            starlette.responses.RedirectResponse: A redirect response to the home page if the user is authenticated.

        Raises:
            HTTPException: A HTTP exception with status code 401 if the user is not authenticated.
        """
    if users.verify_user(email, password):
        token = users.manager.create_access_token(data=dict(sub=email))
        response = RedirectResponse("/home", status_code=302)
        users.manager.set_cookie(response, token)
        return response

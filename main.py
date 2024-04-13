from urllib import request

from fastapi import FastAPI, Request, Form
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi_login import LoginManager
from starlette.responses import RedirectResponse

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
@app.get("/index")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/dashboard")
async def dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})


@app.get("/input")
async def input(request: Request):
    return templates.TemplateResponse("input.html", {"request": request})


@app.get("/home")
async def home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/signup")
async def signup(request: Request):
    return templates.TemplateResponse("signup.html", {"request": request})


@app.post("/signup")
async def signup_user(request: Request, first_name=Form(), last_name=Form(), email=Form(), password=Form()):
    users.make_user(first_name, last_name, email, password)
    token = users.manager.create_access_token(data=dict(sub=email))
    response = RedirectResponse("/home")
    users.manager.set_cookie(response, token)
    return response


@app.get("/login")
async def login(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})


@app.post("/login")
async def login_user(request: Request, email=Form(), password=Form()):
    if users.verify_user(email, password):
        token = users.manager.create_access_token(data=dict(sub=email))
        response = RedirectResponse("/home")
        users.manager.set_cookie(response, token)
        return response

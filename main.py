from urllib import request

from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
# Making the initial app
app = FastAPI()
# Adding all the statis files to the webserver
app.mount("/static", StaticFiles(directory="static"), name="static")
# Making the templating engine
templates = Jinja2Templates("templates")
# Initializing the database


# Rendering Pages
@app.get("/")
async def index(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})


@app.get("/status/{test_a}")
async def status_testa(test_a: int):
    return {"testa": test_a * 2}

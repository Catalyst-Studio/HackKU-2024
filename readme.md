# Getting Started
The main purpose of this repository is to teach you some of the basics of how to make a functional website using FastAPI and Halfmoon CSS. You are expected to have some previous knowledge of python and how the web works. This is not a beginner project to learn how the web works and how to make Full Stack applications, but more of a way for you to understand the principles and methods that are used by these frameworks and technologies.
## Setup
Follow the following instructions to set up the repository on your computer
#### Pull the repository
In the directory that you want to download the project execute the following command
```commandline
git clone https://gitea.catalyst-studios.cc/Hackathon-Helpers/Learning-FastAPI.git
```
#### Go into the project directory
```commandline
cd ./Learning_FastAPI
```
#### Create a virtual environment
To allow for easy package management and python version management run the following command to create a virtual environment
```commandline
# replace the <python install> with your python installation, default: python
<python install> -m venv venv
```
Then execute the following command
###### Windows
```commandline
venv\Scripts\activate
```
###### MacOS or Unix-like
```commandline
source venv/bin/activate
```
#### Install package requirements
The following command will install all packages required for the repository to run initially
```commandline
python -m pip install -r requirements.txt
```
#### Run the program
We will use [uvicorn](https://www.uvicorn.org) to run the ASGI Webserver (FastAPI)
```commandline
python -m uvicorn main:app
```
# The Goal
The goal of the project is to create a QR Code Generator using the code provided. The database is provided using SQL Alchemy and is a [SQLite](https://www.sqlite.org) file that resets everytime you restart the application. 
### Level 1 The Front End
In level one your goal should be to make and design a user interface for the QR Code Generator; it should include the following
- An input for the user to paste the content they want the QR Code to contain
  - Optionally it can include a file upload section for the QR Code to contain files/images
- A multi-select for the user to select what properties they want for the QR Code (see qrcode.py for the options)
- A preview of the QR Code that updates at least one second after the user stops typing in the content input field
- A submit button to take the user to the Qr Code Export page
- A second page called the QR Code Export page that includes the following
  - A user input for the dimensions of the QR Code
  - A user input for the filetype EX: png, jpeg, webp
  - A submit button to download the image file of the QR Code
### Level 2 The Backend
In Level two your goal should be to make and design the api endpoints (located in api.py) that the user interface will interact with; it should include the following
- A preview endpoint that will take all the options that the user provided and the content of the QR Code and generate a QR Code meeting that criteria that will always be 200x200 px
- A submit endpoint that will talke all the options that the user provided and the content of the QR Code and store it somewhere for later use and then redirect the user to the QR Code Export page to download there QR Code
- An Export endpoint that will use the previously saved user provided details and the newly provided dimensions and filetype and returns the image of the QR Code
### Level 3 Saved QR Codes (Challenge)
In level three your goal should be to make and design the front and back end of a page that will save all qr codes and there options so the user can access them later; it should include the following
- A list_qrcodes endpoint that will return a list of all the qr codes that the user has generated and will then display. it should include a preview of the image in a byte64 format
- A View QR Codes page that will allow you to view all the QR Codes that the user has generated in a grid format that includes a preview of the QR Code and the data it was generated; sorted by date last downloaded
  - Should also include two buttons that are "Download" and "Edit" that will let you download the QR Code using the latest export settings and modify the QR Code export settings
# What you will learn
#### Programming Languages
- Python
- HTML (Technically not a programming language, but a mark-up language)
- CSS
- JavaScript
#### Technologies
- [Jinja2](https://palletsprojects.com/p/jinja/)
- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [SQLite](https://www.sqlite.org/)
- [Virtual Environment](https://packaging.python.org/en/latest/keyprojects/#pipenv)
- [Halfmoon CSS](https://www.gethalfmoon.com/) (A drop in Bootstrap replacement)
- [Font Awesome](https://www.fontawesome.com)
# Tips
- Everytime that you install/uninstall a package in python run the following command to keep your requirements updated
```commandline
python -m pip freeze > requirements.txt
```
- Everytime that you update the python code you need to rerun the application
- Everytime that you update the HTML, CSS, or JavaScript you don't need to rerun the application
- Google and Stack Overflow are your friends; use them for help
- Functions for any route of the web application should be defined using async
```python
@app.get("/my_endpoint")
async def my_endpoint(request: Request):
    return True
```
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

base = declarative_base()


# Example model. Delete when actually making program
class ExampleModel(base):
    __tablename__ = 'example'
    id = Column(Integer, primary_key=True)
    my_data = Column(String)

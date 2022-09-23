from email.mime import base
from logging.config import dictConfig
from turtle import st
from unicodedata import name
from pydantic import BaseModel
from typing import Optional

class User(BaseModel):
    id: Optional[str]
    name : str
    lastname: str
    dni : str
    email : str
    password : str 
from pydantic import BaseModel
from sqlalchemy import Column, Integer, String
from sqlalchemy.dialects.postgresql import ARRAY
from sqlalchemy.orm import declarative_base

class User(BaseModel):
    id: int
    name: str = 'Jane Doe'
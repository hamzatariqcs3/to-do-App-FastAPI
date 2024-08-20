# fastapi_project/schemas.py
from pydantic import BaseModel

class UserBase(BaseModel):
    name: str
    password: str
    email: str
    age: str
    address: str
    phone_number: str

class UserCreate(UserBase):
    pass

class User(UserBase):
    id: int

    class Config:
        orm_mode = True

# fastapi_project/userModels.py
from sqlalchemy import Column, Integer, String,ForeignKey,DateTime
from ..database import Base
from sqlalchemy.sql import func

class User(Base):
    __tablename__ = "users"  # Consider using plural for clarity

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(50), nullable=False, index=True)
    password = Column(String(255), nullable=False)
    email = Column(String(120), unique=True, nullable=False, index=True)
    age = Column(Integer, nullable=True)
    address = Column(String(255), nullable=True)
    phone_number = Column(String(20), unique=True, nullable=True, index=True)
    created_at = Column(DateTime, server_default=func.now())
    # Additional columns can be added as required.

# fastapi_project/models.py
from sqlalchemy import Column, Integer, String,ForeignKey,DateTime
from ..database import Base
from sqlalchemy.sql import func

class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    userId = Column(Integer, ForeignKey("users.id"), index=True)
    name = Column(String(50), index=True)  # Specify length for String
    description = Column(String(255), index=True)  # Specify length for String
    created_at = Column(DateTime, server_default=func.now())
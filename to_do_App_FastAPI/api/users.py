from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..models.userModels import User
from .. import dependencies, userSchemas

router = APIRouter()

@router.post("/user/add", response_model=userSchemas.User)
def create_item(user: userSchemas.UserCreate, db: Session = Depends(dependencies.get_db)):
    user_data = user.dict()
    db_user = User(**user_data)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

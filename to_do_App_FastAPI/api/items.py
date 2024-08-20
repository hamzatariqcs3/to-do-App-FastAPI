from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from ..models.models import Item
from .. import dependencies, schemas

router = APIRouter()

@router.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db)):
    item_data = item.dict()
    db_item = Item(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@router.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/search/{item_title}", response_model=schemas.Item)
def read_item_by_name(item_title: str, db: Session = Depends(dependencies.get_db)):
    item = db.query(Item).filter(Item.name.like(f"%{item_title}%")).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@router.get("/items/delete/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    item = db.query(Item).filter(Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    db.delete(item)
    db.commit()
    return item

@router.get("/items/deletewithname/{item_title}", response_model=List[schemas.Item])
def delete_item_by_name(item_title: str, db: Session = Depends(dependencies.get_db)):
    items = db.query(Item).filter(Item.name.like(f"%{item_title}%")).all()
    if not items:
        raise HTTPException(status_code=404, detail="Item(s) not found")
    for item in items:
        db.delete(item)
    db.commit()
    return items

@router.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    items = db.query(Item).offset(skip).limit(limit).all()
    return items

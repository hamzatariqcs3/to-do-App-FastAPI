# fastapi_project/main.py
from fastapi import Depends, FastAPI, HTTPException
from sqlalchemy.orm import Session
from . import models, dependencies, schemas
from .database import engine, Base
from typing import List
Base.metadata.create_all(bind=engine)



app = FastAPI()

@app.post("/items/", response_model=schemas.Item)
def create_item(item: schemas.ItemCreate, db: Session = Depends(dependencies.get_db)):
    item_data = item.dict()
    print(f"****waqas***{item_data}")
    
    db_item = models.Item(**item_data)
    db.add(db_item)
    db.commit()
    db.refresh(db_item)
    return db_item

@app.get("/items/{item_id}", response_model=schemas.Item)
def read_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item

@app.get("/items/search/{item_title}", response_model=schemas.Item)
def read_item_by_name(item_title: str, db: Session = Depends(dependencies.get_db)):
    item = db.query(models.Item).filter(models.Item.name.like(f"%{item_title}%")).first()

    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    return item


@app.get("/items/delete/{item_id}", response_model=schemas.Item)
def delete_item(item_id: int, db: Session = Depends(dependencies.get_db)):
    item = db.query(models.Item).filter(models.Item.id == item_id).first()
    if item is None:
        raise HTTPException(status_code=404, detail="Item not found")
    
    db.delete(item)  # This deletes the item from the database
    db.commit()  # Commit the transaction to persist the changes
    return item  # Optionally, return the deleted item (before deletion)

@app.get("/items/deletewithname/{item_title}", response_model=List[schemas.Item])
def delete_item_by_name(item_title: str, db: Session = Depends(dependencies.get_db)):
    items = db.query(models.Item).filter(models.Item.name.like(f"%{item_title}%")).all()

    if not items:
        raise HTTPException(status_code=404, detail="Item(s) not found")
    
    # Delete each item
    for item in items:
        db.delete(item)
    
    db.commit()  # Commit the transaction to persist the changes
    return items  # Return the list of deleted items


@app.get("/items/", response_model=List[schemas.Item])
def read_items(skip: int = 0, limit: int = 10, db: Session = Depends(dependencies.get_db)):
    items = db.query(models.Item).all()
    return items
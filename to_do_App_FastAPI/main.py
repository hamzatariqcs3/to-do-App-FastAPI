from fastapi import FastAPI
from to_do_App_FastAPI.api import items, users  # Use absolute import path

# Create tables
from to_do_App_FastAPI.database import engine, Base
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Include routers
app.include_router(items.router, prefix="/api")
app.include_router(users.router, prefix="/api")

from fastapi import FastAPI
from .models import Base, engine, User
from .schemas import UserCreate, UserResponse
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel
from typing import List

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post("/users/", response_model=UserResponse)
def create_user(user: UserCreate):
    db = SessionLocal()
    db_user = User(name=user.name)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    db.close()
    return db_user

@app.get("/users/", response_model=List[UserResponse])
def read_users():
    db = SessionLocal()
    users = db.query(User).all()
    db.close()
    return users

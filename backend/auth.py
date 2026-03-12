from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from passlib.context import CryptContext
from jose import jwt
from datetime import datetime, timedelta

import re
router = APIRouter()

SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

from database import users_collection
from datetime import datetime


class User(BaseModel):
    username: str
    password: str


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain, hashed):
    return pwd_context.verify(plain, hashed)


def create_token(data):
    expire = datetime.utcnow() + timedelta(hours=1)
    data.update({"exp": expire})
    return jwt.encode(data, SECRET_KEY, algorithm=ALGORITHM)


@router.post("/signup")
def signup(user: User):

    existing_user = users_collection.find_one({"username": user.username})
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")

    if len(user.password) < 8 or not re.search(r"[a-zA-Z]", user.password) or not re.search(r"[0-9]", user.password):
        raise HTTPException(status_code=400, detail="Password must be at least 8 characters long and include both letters and numbers")

    hashed_pw = hash_password(user.password)
    new_user = {
        "username": user.username,
        "password_hash": hashed_pw,
        "created_at": datetime.utcnow()
    }
    users_collection.insert_one(new_user)

    return {"message": "User created successfully"}


@router.post("/login")
def login(user: User):

    db_user = users_collection.find_one({"username": user.username})
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    hashed = db_user.get("password_hash")

    if not verify_password(user.password, hashed):
        raise HTTPException(status_code=401, detail="Invalid credentials")

    token = create_token({"sub": user.username})

    return {"access_token": token}
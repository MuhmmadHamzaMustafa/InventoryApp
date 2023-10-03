from fastapi import APIRouter, Depends
from typing import List
from models import UserModel

router = APIRouter()

@router.post("/users/", response_model=UserModel)
def create_user(user: UserModel):
    return user

@router.get("/users/", response_model=List[UserModel])
def get_users():
    return []

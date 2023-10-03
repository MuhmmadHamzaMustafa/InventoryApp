from fastapi import APIRouter, Depends
from typing import List
from models import CategoryModel

router = APIRouter()

@router.post("/categories/", response_model=CategoryModel)
def create_category(category: CategoryModel):
    return category

@router.get("/categories/", response_model=List[CategoryModel])
def get_categories():
    return []


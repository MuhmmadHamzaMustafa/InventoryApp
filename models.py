from pydantic import BaseModel
from typing import List, Optional

# User Model
class UserModel(BaseModel):
    username: str
    email: str
    role: str

# Category Model
class CategoryModel(BaseModel):
    category_name: str

# Product Model
class ProductModel(BaseModel):
    product_name: str
    description: str
    price: float
    category_id: int

# Sale Model
class SaleModel(BaseModel):
    user_id: int
    product_id: int
    quantity_sold: int
    sale_date: str
    category_id: int # You may want to add this field if you have a category for each sale

# Response Model for Revenue Analysis
class RevenueComparisonResponseModel(BaseModel):
    period: str
    category_id: int
    total_revenue: float

# Inventory Model
class InventoryModel(BaseModel):
    product_id: int
    current_quantity: int

# Query Parameters for Sales Analysis
class SalesQueryParams(BaseModel):
    start_date: str
    end_date: str
    product_id: Optional[int] = None
    category_id: Optional[int] = None

# Response Models
class SalesResponseModel(BaseModel):
    sale_id: int
    user_id: int
    product_id: int
    quantity_sold: int
    sale_date: str
    revenue: float

class InventoryResponseModel(BaseModel):
    inventory_id: int
    product_id: int
    current_quantity: int
    last_updated: str

# Response Model for Revenue Comparison
class RevenueComparisonResponseModel(BaseModel):
    period: str
    category_id: int
    total_revenue: float

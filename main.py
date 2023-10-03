from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import Session, sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from models import SaleModel, RevenueComparisonResponseModel, InventoryModel
from routers import users, categories, products, sales, inventory

# Create the FastAPI app
app = FastAPI()

# Configure the database connection (SQLite in this example)
DATABASE_URL = "sqlite:///./test.db"
engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the base class for SQLAlchemy models
Base = declarative_base()

# Define your SQLAlchemy models here (replace with actual tables and relationships)
class Sale(Base):
    __tablename__ = "sales"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    product_id = Column(Integer)
    quantity_sold = Column(Integer)
    sale_date = Column(String)
    category_id = Column(Integer)

class Inventory(Base):
    __tablename__ = "inventory"
    id = Column(Integer, primary_key=True, index=True)
    product_id = Column(Integer)
    current_quantity = Column(Integer)

# Create tables in the database
Base.metadata.create_all(bind=engine)

# Dependency to get the database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Import your routers and include them in the app
from routers import users, categories, products, sales, inventory

app.include_router(users.router)
app.include_router(categories.router)
app.include_router(products.router)
app.include_router(sales.router)
app.include_router(inventory.router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)

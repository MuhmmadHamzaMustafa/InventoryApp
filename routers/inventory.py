from fastapi import APIRouter, HTTPException, Query
from typing import List, Optional
from models import InventoryModel

router = APIRouter()

# Dummy inventory data
inventory_data = [
    InventoryModel(product_id=1, current_quantity=100),
    InventoryModel(product_id=2, current_quantity=50),
    InventoryModel(product_id=3, current_quantity=75),

]

@router.get("/inventory/")
def get_inventory(
    product_id: Optional[int] = Query(None, description="Filter by product ID"),
    low_stock_alert: Optional[bool] = Query(False, description="Show low stock alerts"),
) -> List[InventoryModel]:
    if product_id is not None:
        inventory = [item for item in inventory_data if item.product_id == product_id]
    else:
        inventory = inventory_data

    if low_stock_alert:
        inventory = [item for item in inventory if item.current_quantity < 20]

    return inventory

@router.put("/inventory/{product_id}/")
def update_inventory(
    product_id: int,
    new_quantity: int,
) -> InventoryModel:
    for item in inventory_data:
        if item.product_id == product_id:
            item.current_quantity = new_quantity
            return item

    raise HTTPException(status_code=404, detail="Product not found")

@router.delete("/inventory/{product_id}/")
def delete_inventory(product_id: int) -> str:
    global inventory_data
    inventory_data = [item for item in inventory_data if item.product_id != product_id]
    return f"Product with ID {product_id} has been deleted from inventory."

@router.post("/inventory/")
def add_product_to_inventory(item: InventoryModel) -> InventoryModel:
    inventory_data.append(item)
    return item

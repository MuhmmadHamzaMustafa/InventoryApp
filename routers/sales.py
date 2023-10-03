from fastapi import APIRouter, Query, HTTPException
from datetime import date, timedelta
from typing import List, Optional, Dict
from models import SaleModel, RevenueComparisonResponseModel

router = APIRouter()

# Dummy sales data
sales_data = [
    SaleModel(user_id=1, product_id=1, quantity_sold=10, sale_date="2023-01-01", category_id=1),
    SaleModel(user_id=2, product_id=2, quantity_sold=5, sale_date="2023-01-02", category_id=2),
    SaleModel(user_id=1, product_id=1, quantity_sold=8, sale_date="2023-01-03", category_id=1),
]

def calculate_revenue(
    period: str,
    sales: List[SaleModel],
    category_id: Optional[int] = None
) -> Dict[str, float]:
    revenue_data = {}
    today = date.today()

    if category_id is not None:
        sales = [sale for sale in sales if sale.category_id == category_id]

    if period == "daily":
        start_date = today - timedelta(days=1)
    elif period == "weekly":
        start_date = today - timedelta(weeks=1)
    elif period == "monthly":
        start_date = today - timedelta(days=30)
    elif period == "annual":
        start_date = today - timedelta(days=365)
    else:
        raise HTTPException(status_code=400, detail="Invalid period")

    filtered_sales = [sale for sale in sales if date.fromisoformat(sale.sale_date) >= start_date]

    total_revenue = sum(sale.quantity_sold * 100 for sale in filtered_sales)
    revenue_data[period] = total_revenue

    return revenue_data

@router.get("/revenue/")
def get_revenue(
    period: str = Query(..., description="Period for revenue analysis (daily, weekly, monthly, annual)"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
) -> Dict[str, float]:
    revenue_data = calculate_revenue(period, sales_data, category_id)
    return revenue_data

@router.get("/compare-revenue/")
def compare_revenue(
    start_date: date = Query(..., description="Start date for comparison"),
    end_date: date = Query(..., description="End date for comparison"),
    category_id: Optional[int] = Query(None, description="Filter by category ID"),
) -> List[RevenueComparisonResponseModel]:
    comparison_data = []

    for period in ["daily", "weekly", "monthly", "annual"]:
        revenue_data = calculate_revenue(period, sales_data, category_id)
        comparison_data.append(RevenueComparisonResponseModel(period=period, category_id=category_id, total_revenue=revenue_data[period]))

    return comparison_data

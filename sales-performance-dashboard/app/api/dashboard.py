from fastapi import APIRouter
from app.services.sales_service import sales_service

router = APIRouter()

@router.get("/summary")
def get_summary():
    return sales_service.get_summary()

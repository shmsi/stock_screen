from fastapi import APIRouter
from .data_stream import redis_client

router = APIRouter()


@router.get("/stock_price")
def get_latest_stock_price():
    return {"stock_price": redis_client.get("latest_stock_price")}

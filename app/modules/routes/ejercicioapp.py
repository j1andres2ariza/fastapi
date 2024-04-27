from fastapi import APIRouter, Depends, HTTPException
from .strategy import OrderSend, OrderUponDelivery, Orders, OrderVirtual
from enum import Enum


class Order(Enum):
    SEND = "send"
    UPON_DELIVERY = "upon_delivery"
    VIRTUAL = "virtual"

def get_strategy(order: Order) -> Orders:
    if order == Order.SEND:
        return OrderSend()
    elif order == Order.UPON_DELIVERY:
        return OrderUponDelivery()
    elif order == Order.VIRTUAL:
        return OrderVirtual()
    else:
        raise HTTPException(status_code=400, detail="Invalid order")


router = APIRouter()

@router.get("/info_order")
def info_order(origin: int, destination: int, order: Orders = Depends(get_strategy)) -> dict:
    return order.get_info_order(origin=origin, destination=destination)

@router.get("/cost")
def cost(origin: int, destination: int, order: Orders = Depends(get_strategy)) -> float:
    return order.get_cost(origin=origin, destination=destination)

@router.get("/duration")
def duration(origin: int, destination: int, order: Orders = Depends(get_strategy)) -> float:
    return order.get_duration(origin=origin, destination=destination)
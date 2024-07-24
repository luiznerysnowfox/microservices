from fastapi import FastAPI
from .models import Base, engine, Order
from .schemas import OrderCreate, OrderResponse
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post("/orders/", response_model=OrderResponse)
def create_order(order: OrderCreate):
    db = SessionLocal()
    db_order = Order(product_id=order.product_id, quantity=order.quantity)
    db.add(db_order)
    db.commit()
    db.refresh(db_order)
    db.close()
    return db_order

@app.get("/orders/", response_model=List[OrderResponse])
def read_orders():
    db = SessionLocal()
    orders = db.query(Order).all()
    db.close()
    return orders

from fastapi import FastAPI
from .models import Base, engine, Product
from .schemas import ProductCreate, ProductResponse
from sqlalchemy.orm import sessionmaker
from typing import List

app = FastAPI()
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

@app.post("/products/", response_model=ProductResponse)
def create_product(product: ProductCreate):
    db = SessionLocal()
    db_product = Product(name=product.name, price=product.price)
    db.add(db_product)
    db.commit()
    db.refresh(db_product)
    db.close()
    return db_product

@app.get("/products/", response_model=List[ProductResponse])
def read_products():
    db = SessionLocal()
    products = db.query(Product).all()
    db.close()
    return products

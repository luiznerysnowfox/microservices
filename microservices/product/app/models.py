from sqlalchemy import Column, Integer, String, Float
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "postgresql://postgres:password@db:5432/postgres"
engine = create_engine(SQLALCHEMY_DATABASE_URL)
Base = declarative_base()

class Product(Base):
    __tablename__ = "products"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    price = Column(Float)

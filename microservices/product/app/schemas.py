from pydantic import BaseModel

class ProductCreate(BaseModel):
    name: str
    price: float

class ProductResponse(BaseModel):
    id: int
    name: str
    price: float

    class Config:
        orm_mode = True

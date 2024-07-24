from pydantic import BaseModel

class OrderCreate(BaseModel):
    product_id: int
    quantity: int

class OrderResponse(BaseModel):
    id: int
    product_id: int
    quantity: int

    class Config:
        orm_mode = True

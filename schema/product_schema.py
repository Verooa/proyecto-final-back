from pydantic import BaseModel
from typing import Optional

class ProductInput(BaseModel):
    name: str
    description: str
    price: float
    stock: int
    category: str

class ProductSchema(ProductInput):
    id: Optional[int]
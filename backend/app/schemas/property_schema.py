from pydantic import BaseModel

class Property(BaseModel):
    title: str
    price: float
    address: str
    description: str = ""
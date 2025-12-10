from baseWithId import BaseWithId
from pydantic import BaseModel

class ProductBase(BaseWithId):
    name : str
    price : float
    @property 
    def product_id(self):
        return self.id

class ProductUpdate(BaseModel):
    product_id: int | None
    name : str | None
    price : float | None
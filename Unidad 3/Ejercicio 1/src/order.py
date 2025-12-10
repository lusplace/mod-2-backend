from product import *
from baseWithId import BaseWithId
from pydantic import BaseModel
import json

class OrderBase(BaseWithId):
    product_dict : dict = {}
    @property
    def order_id (self): 
        return self.id

    def modify_order(self, product_id: int, quantity: int = 1):
        if self.product_dict.get(product_id):
            self.product_dict[product_id] += quantity
        else: 
            self.product_dict[product_id] = quantity
        if self.product_dict[product_id] <= 0:
            self.product_dict.pop(product_id)

    def to_dict(self):
        # Return a simple, serializable dictionary
        tmp = []
        json_dict = {'order_id': self.order_id}

        json_dict.update({'product_dict': self.product_dict})
        
        return json_dict
    

class OrderUpdate(BaseModel):
    id : int
    product_id : int
    quantity : int

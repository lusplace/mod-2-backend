from pydantic import BaseModel
from product import *

class OrderBase(BaseModel):
    product_dict : []
    order_id : int

    def addToOrder(product_id: int, quantity: int = 1):
        if quantity < 1: 
            raise error
        if product_dict[product_id]:
            product_dict[product_id] += quantity

class ProductInOrder():
    def __init__(self, product : ProductBase, quantity: int):
        self.product = product
        self.quantity = quantity

class OrderNode():

    def __init__(self, order : OrderBase, prev : OrderNode | None = None, next: OrderNode | None = None):
        self.hash = hash(order.order_id)
        self.order = order
        self.prev = prev
        self.next = next

class OrderUpdate(BaseModel):
    order_id : int | None
    next_order: int | None 
    prev_order: int | None


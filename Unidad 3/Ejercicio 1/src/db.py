from product import *
from order import *
from bintrees import AVLTree
import json
from typing import TypeVar, List, Generic, Optional
import array
from linkedList import *

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class dbConnection(metaclass=Singleton):

    def __init__(self, products_mock_file : str = "./mock_products.json", orders_mock_file : str = "./mock_orders.json"):
        self.data_file = products_mock_file
        self.product_tree = dbConnection.init_tree(products_mock_file)
        self.linked_orders = dbConnection.init_order_list(orders_mock_file)

    def init_tree(products_mock_file) -> AVLTree:
        data = []
        try:
            with open(products_mock_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{products_mock_file}' was not found.")
        tree = AVLTree()
        number_of_mistakes = 0

        for item in data:
            if(is_valid_product(item)):
                tree.insert(hash(item.get('product_id')), item)
            else:
                print(f"{item} not valid")
        if(number_of_mistakes > 0):
            print(f"elements inserted with {number_of_mistakes} errors")
        else:
            print("DB Setup successfull!")
        return tree

    def init_order_list(self) -> LinkedList:
        linkedList = LinkedList(OrderBase)
        return linkedList

        data = []
        try:
            with open(orders_mock_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{orders_mock_file}' was not found.")
        number_of_mistakes = 0

        for item in data:
            if(is_valid_order(item)):
                linkedList.insert(hash(item.get('order_id')), item)
            else:
                print(f"{item} not valid")
        if(number_of_mistakes > 0):
            print(f"elements inserted with {number_of_mistakes} errors")
        else:
            print("DB Setup successfull!")
        return linkedList

    def insert_product(self, product : ProductBase) -> bool:
        try:
            key = hash(product.product_id)
            self.product_tree.insert(key, product)
            status = True
        except: 
            print("Error inserting Product")
            status = False
        return status
        
    def remove_product(self, product_id: int) -> ProductBase | None:
        wait_time = 0
        if self.product_tree is None:
            self.product_tree = init_tree()

        try:
            removed = self.product_tree.pop(hash(product_id))
            print(removed)
        except:
            print("error occurred")
            removed = None
        return removed

    def get_product(self, product_id: int) -> ProductBase | None:
        try:
            product = self.product_tree.get(hash(product_id))
        except:
            print("error occurred")
            product = None
        return product

    def create_order(self, id : int):
        order = OrderBase(id = id)
        result = self.linked_orders.insert_at_beginning(order)
        return result

    def get_order(self, id : int):
        order = self.linked_orders.getNode(id)
        return order.to_dict()
    
    def get_all_orders(self):
        orders = self.linked_orders.all_values()
        return orders

    def update_order(self, orderUpdate:OrderUpdate) -> OrderBase | str:
        order_id = orderUpdate.id

        orderNode = self.linked_orders.getNode(order_id)
        if orderNode is None: return 
        order = orderNode.value
        productId = orderUpdate.product_id

        if self.get_product(productId) is not None:
            order.modify_order(productId, orderUpdate.quantity)
            mod_order = self.linked_orders.setNode(order)
            return mod_order.to_dict()
        else: 
            return f"Product {productId} Not Found"
        return None


def is_valid_product(item):
    p_id = item.get('product_id')
    p_name = item.get('name')
    p_price = item.get('price')
    if p_id is None or p_name is None or p_name == 0 or p_price is None:
        return False
    return True
from product import *
from bintrees import AVLTree
import json

class Singleton(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

class dbConnection(metaclass=Singleton):

    def __init__(self, products_mock_file : str = "./mock_products.json", orders_mock_file : str = "./mock_orders.json"):
        self.data_file = products_mock_file
        self._lock = False
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

    def init_order_list(orders_mock_file) -> LinkedList:
        data = []
        try:
            with open(orders_mock_file, 'r') as file:
                data = json.load(file)
        except FileNotFoundError:
            print(f"Error: The file '{orders_mock_file}' was not found.")
        linkedList = LinkedList()
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
        self.get_lock()
        try:
            key = hash(product.product_id)
            self.product_tree.insert(key, product)
            status = True
        except: 
            print("Error inserting Product")
            status = False
        finally:
            self.release_lock()
        return status
        
    def remove_product(self, product_id: int) -> ProductBase | None:
        wait_time = 0
        while self._lock:
            time.wait(0.5)
            wait_time += 0.5
            print(f"waiting for {wait_time}")
        self._lock = True
        if self.product_tree is None:
            self.product_tree = init_tree()

        try:
            removed = self.product_tree.pop(hash(product_id))
            print(removed)
        except:
            print("error occurred")
            removed = None
        finally:
            self._lock = False
        return removed

    def get_product(self, product_id: int) -> ProductBase | None:

        self.get_lock()
        try:
            product = self.product_tree.get(hash(product_id))
        except:
            print("error occurred")
            product = None
        finally:
            self.release_lock()
        return product

    def get_lock(self):
        wait_time = 0
        while self._lock:
            time.wait(0.5)
            wait_time += 0.5
            print(f"waiting for {wait_time}")
        self._lock = True
    
    def release_lock(self):
        if not self._lock:
            print("DB might be compromised")
        self._lock = False


def is_valid_product(item):
    p_id = item.get('product_id')
    p_name = item.get('name')
    p_price = item.get('price')
    if p_id is None or p_name is None or p_name == 0 or p_price is None:
        return False
    return True

def is_valid_order(item):
    ## TODO
    p_id = item.get('order_id')
    p_name = item.get('name')
    p_price = item.get('price')
    if p_id is None or p_name is None or p_name == 0 or p_price is None:
        return False
    return True
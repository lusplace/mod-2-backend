from product import *
from db import dbConnection
import json
from fastapi import FastAPI
from bintrees import AVLTree
from fastapi.responses import JSONResponse
from order import *

db = dbConnection()

app = FastAPI()

@app.on_event("startup")
def on_startup():
    db = dbConnection()

#a. Crear un producto.\
@app.post("/products/add")
async def add_product(product: ProductBase):

    product_dict = product.dict()
    try:
        p_id = product_dict['product_id']
        p_name = product_dict['name']
        p_price = product_dict['price']
    except KeyError:
        return JSONResponse(content=f"product not valid", status_code=403)

    if db.insert_product(product):
        return JSONResponse(content=f"product {p_name} inserted successfully", status_code=201)
    else:
        return JSONResponse(content=f"product {p_name} failed", status_code=400)

#b. Consultar información de producto por ID.\
@app.get("/products/{id}")
async def get_product(id: int):
    product = db.get_product(id)
    if product is None:
            return JSONResponse(content=f"Product {id} not found", status_code=404)
    return JSONResponse(content=product, status_code=200)

#c. Crear nuevo pedido.\
@app.post("/orders/add/{id}")
async def create_order(id: int):
    try:
        order = db.create_order(id)
        if order is not None:
            return JSONResponse(content=order.to_dict(), status_code=200)
    except Exception as e:
        print("The error is: ",e)
    return JSONResponse(content=f"order {id} already exists", status_code=403)

#d. Consultar información de pedido por ID.\
@app.get("/orders/{id}")
async def get_order(id: int):
    try:
        order = db.get_order(id)
        return JSONResponse(content=order, status_code=200)
    except Exception as e:
        print("The error is: ",e)
        return JSONResponse(content=f"order {id} doesnt exist", status_code=404)

#e. Actualizar un pedido existente.\
@app.patch("/orders/update")
async def update_order(order: OrderUpdate):
    try:
        order = db.update_order(order)
        if(order is not None):
            return JSONResponse(content=order, status_code=200)
    except Exception as e:
        print("The error is: ",e)
    return JSONResponse(content=f"order {id} doesnt exist", status_code=404)

#f. Eliminar un pedido.\
@app.delete("/orders/delete/{id}")
async def delete_order(id: int):
    try:
        order = db.delete_order(id)
        return JSONResponse(content=f"order {id} deleted", status_code=200)
    except Exception as e:
        print("The error is: ",e)
        return JSONResponse(content=f"order {id} doesnt exist", status_code=404)

#g. Listar todos los pedidos.
@app.get("/orders/")
async def get_all_orders():
    try:
        orders = db.get_all_orders()
        return JSONResponse(content=orders, status_code=200)
    except Exception as e:
        print("The error is: ",e)
        return JSONResponse(content=f"order {id} doesnt exist", status_code=404)

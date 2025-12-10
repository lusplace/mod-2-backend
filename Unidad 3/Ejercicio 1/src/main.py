from product import *
from db import dbConnection
import json
from fastapi import FastAPI
from bintrees import AVLTree
from fastapi.responses import JSONResponse

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

#d. Consultar información de pedido por ID.\
#e. Actualizar un pedido existente.\
#f. Eliminar un pedido.\
#g. Listar todos los pedidos.

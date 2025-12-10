# mod-2-backend
Ejercicios en el master de desarrollo web

Aquí las instrucciones del ejercicio más reciente
## Unidad 3: Serialización

>**disclaimer** Se ha utilizado el término order para *pedido* y *product* para producto en este ejercicio.

### RUN THE PROJECT

1. Ubícate en
>cd Unidad 3/Ejercicio 1/
2. Convierte run.sh en ejecutable (Mira 2.5 si no estás en linux)
> chmod +x ./run.sh

3. Ejecuta
> ./run.sh

2.5. O ejecuta las 3 sentencias en él (ignora el paso 3 en este caso)

> pip install -r ./requirements.txt
> fastapi run ./main.py

4. Para salir

>Ctrl + C 
en la consola en la que s eejecuta el proyecto

### Dependencias del proyecto

Este campo no cubre lo presente en archivos requirements.txt para python

python 3.10
pip

### Probado en 

POP!_Os 22.04
(Equivalente a Ubuntu 22.04 a nivel técnico)

### Lista de llamadas a la API

Con url base 127.0.0.1:8000

#### Products
 - /products/{id}
    - Get básico para un producto, hay 50 como mock
 - /products/add
    - Ejemplo de Body de la request
>   
    {
        "product_id": 1024,
        "name": "FooBar",
        "price": 66.99
    }

#### Orders

 - /orders/add/{id}
    - Obtiene una petición u order por id, inicialmente hay 50 cargados
 - /orders
 - /orders/update
    - El cuerpo de la request no es un objeto *order* al uso, sino que obedece a añadir un número *quantity* (que puede ser negativo, siendo que dejando la cantidad de un producto en 0 o menos se elimina el id de producto del objeto order) del producto con un identificador *product_id* para verificar que el producto existe.
    Ejemplo de *body* de la request

>
    {   
        "id": 9,
        "product_id": 34,
        "quantity": 33
    }


#### Serialización
 - Se ha implementado una función to_dict oara convertir los objetos precisos en un diccionario, lo que es en sí un objeto de javascript.



### Anotaciones y Comentarios

Hash: El hash automatico que he utilizado, esta en una función en la clase BasewithId.
Efectivamente para este proyecto devuelve el valor id que le pases, como *str*.




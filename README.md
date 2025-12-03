# mod-2-backend
Ejercicios en el master de desarrollo web

## Unidad 2 Ejercicio 1: API con Fastapi e integración de SPOTIFY

### RUN THE PROJECT

1. Ubícate en
>cd Unidad 2/Ejercicio 1/
2. COnvierte run.sh en ejecutable
> chmod +x ./run.sh

3. Ejecuta
> ./run.sh

2.5. O ejecuta las 3 sentencias en él (ignora el paso 3 en este caso)

> docker compose up -d
> pip install -r ./requirements.txt
> fastapi run ./main.py

4. Para salir

>Ctrl + C 
en la consola en la que s eejecuta el proyecto

>docker container ls
busca el contenedor de nombre 'ejercicio1-db-1'
y anota el CONTAINER_ID, que llamaremos IDENTIFICADOR

ejecuta:
>docker docker container kill IDENTIFICADOR

### Dependencias del proyecto

Este campo no cubre lo presente en archivos requirements.txt para python

docker
docker compose
python 3.10
pip

### Probado en 

POP!_Os 22.04
(Equivalente a Ubuntu 22.04 a nivel técnico)

### Modelo de .env

Estos valores se usarán en el contenedor y en la aplicación

Ubicación respecto del repositorio:
/Unidad 2/Ejercicio 1/.env

#### Ejemplo:
export SPOTFY_URI="http://127.0.0.1:PUERTO"
export CLIENT_ID="CLIENTID"
export CLIENT_SECRET="CLIENTSECRET"

export MYSQL_ROOT_PASSWORD= "PASSWORD"
export MYSQL_DATABASE= "DATABASENAME"
export MYSQL_USER= "USER"
export MYSQL_ROOT_USER= "root"
export MYSQL_PASSWORD= "PASSWORD"
export MYSQL_HOST= "127.0.0.1"
export MYSQL_PORT= "PORT"

export HOST_LOCATION= "127.0.0.1:8000"

### Anotaciones y Comentarios

EL volumen de docker con los datos se guardará en la carpeta /Unidad 2/Ejercicio 1/local

(El gitignore contempla no añadir estos archivos)

init.sql no se ejecuta, pero en el codigo python se realiza la misma creación de tablas de no existir las mismas.

Estos datos se moveran a archivos .md o ipynb en la carpeta 'Unidad 2/Ejercicio 1' a futuro

Deuda técnica: mover funciones a sus propios archivos y usar patrones de diseño adecuados.

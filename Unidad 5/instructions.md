## Unidad 5 DJANGO AVANZADO: EJERCICIO 

### RUN THE PROJECT

1. Ubícate en
>cd Unidad 5/
2. Convierte run.sh en ejecutable
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
busca el contenedor de nombre 'unidad5-db-1'
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

#### IMPORTANTE

Usando distribuciones como Ubuntu requieres ejecutar:
> sudo apt-get install pkg-config

Dado que el requisito <code>mysqlclient</code> lo necesita

### Modelo de .env

Estos valores se usarán en el contenedor y en la aplicación

Ubicación respecto del repositorio:
/Unidad 5/.env

#### Ejemplo:
\
export MYSQL_ROOT_PASSWORD= "PASSWORD"\
export MYSQL_DATABASE= "DATABASENAME"\
export MYSQL_USER= "USER"\
export MYSQL_ROOT_USER= "root"\
export MYSQL_PASSWORD= "PASSWORD"\
export MYSQL_HOST= "127.0.0.1"\
export MYSQL_PORT= "PORT"\

export DJANGO_SUPERUSER_USERNAME="admin"\
export DJANGO_SUPERUSER_PASSWORD="password"\
export DJANGO_SUPERUSER_EMAIL="admin@example.com"\
export DJANGO_SUPERUSER_FIRST_NAME="example"\

#

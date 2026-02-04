# Pasos de la migración a DB MYsql

## Requisitos

### Data Dump

>cd Unidad\ 5

>python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > datadump.json

### DB Data origin

sqlite

### DB Data New Location

.env
mysql:8

#### Docker Compose

Datos en env para que no haya fallos.

### Operaciones:

>python3 manage.py dumpdata --natural-foreign --natural-primary -e contenttypes -e auth.Permission --indent 4 > datadump.json

>python3 manage.py migrate

>python manage.py loaddata datadump.json

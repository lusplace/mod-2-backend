# mod-2-backend
Ejercicios en el master de desarrollo web
## ÍNDICE DE EJERCICIOS
### Unidad 2

> Unidad 2/Ejercicio 1
### Unidad 3

> Unidad 3/Ejercicio 1
### Unidad 4

> ejercicio django
(Casi uno de unidad 5 mal hecho por lo que he metido)
Aquí las instrucciones del ejercicio más reciente, de lo cual hay copia en su carpeta

### RUN THE PROJECT

1. Ubícate en
>cd ejercicio_django
(ya estas aquí)
2. Convierte run.sh en ejecutable (Mira 2.5 si no estás en linux)
> chmod +x ./run.sh

3. Ejecuta
> ./run.sh

2.5. O ejecuta las 2 sentencias en él (ignora el paso 3 en este caso)

> pip install -r ./requirements.txt
> python manage.py runserver

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

### Pruebas del proyecto

Las estructuras del proyetco se han regustrado en los archivos admin.py locales con clases admin para ser accesibles desde localhost:8000/admin con la UI de admin de django, aparte de las peticiones a la API 

#### EN CASO DE HACER MODIFICACIONES A LOS MODELOS

ejecutar:
> python manage.py makemigrations
> python manage.py migrate --run-syncdb

### Lista de llamadas a la API y Observaciones

Con url base 127.0.0.1:8000

#### music

Todas las siguientes comienzan con la URL base +
>/music/
Tal que
>127.0.0.1:8000/music/preferences
La variable pref_type debe tomar el valor "track", "artist" o "album" en todas sus apariciones.

La variable username es unica para los modelos personalizados usados en este proyecto.

##### POST
127.0.0.1:8000/music/preferences/add
>
    {
        "pref_type": "track",
        "username": "ddddd",
        "spotify_id": "5W8YXBz9MTIDyrpYaCg2Ky"
    }


##### GET 
> 127.0.0.1:8000/music/preferences
> 127.0.0.1:8000/music/preferences/\<username\>
Objeto preferencias de un solo usuario
> 127.0.0.1:8000/music/preferences/\<username\>/\<pref_type\>
Objeto preferencias de un tipo soportado de un usuario

##### DELETE
> 127.0.0.1:8000/music/preferences/clear/user/\<username\>/type/\<pref_type\>"
> 127.0.0.1:8000/music/preferences/clear/user/\<username\>/

Deja vacía la lista de preferencias de un usuario.

No se borran los objetos de la DB por ser ligeros y poder compartirlos entre usuarios.

Originalmente no iban a tener las etiquetas 'user' y 'type', pero django no me lo acepta, dando el delete como prohibido sin añadir detalles para evitar realizar esta operación por accidente.

#### userManager

Se ha heredado de la clase User de django para aprender a usarla, pero este proyecto no se debe usar en la práctica hasta implementar seguridad en los usuarios.

##### GET
> 127.0.0.1:8000/users/
listar usuarios

> 127.0.0.1:8000/users/username/<str:username>"name="get_users"
Obtener un usuario específico
> 127.0.0.1:8000/users/get
Obtener una lista de usuarios filtrando porque sus parámetros contengan uno o más de los siguientes (usa el filtro icontains): 'username', 'email', 'first_name', 'last_name'.
Ejemplo:
127.0.0.1:8000/users/get?name=john
un parámetro incompleto colabora en la búsqueda

##### POST
> 127.0.0.1:8000/users/add
>
    {
    "username": "ddddd",
    "first_name": "bbbb",
    "last_name": "",
    "email": "eeeeeee@example.com",
    "phone_number": 99999,
	"password": "aabbbbaaa"
    }

##### DELETE
> 127.0.0.1:8000/users/delete/username/<str:username>

Borrado por nombre de usuario EXACTO

##### PUT (También PATCH)
> 127.0.0.1:8000/users/update
update por nombre de usuario EXACTO.
los valores nulos, de longitud 0 o similares serán ignorados.

Usa un requestbody similar al de añadir usuarios, el campo username es para encontrarlo, no se puede cambiar. En produccion mejor usaremos un id unico que el usuario no conozca, para poder implementar cambiarlo con menos problemas.
>
    {
    "username": "ddddd",
    "first_name": "bbbb",
    "last_name": "",
    "email": "",
    "phone_number": 123456789,
	"password": "aabbbbaaa"
    }


#### Serialización

Se utiliza esta pipeline siempre que es preciso
 - función par obtener objetos como ```users = User.objects.all()```

 - data = serializers.serialize("json", users)
 - return JsonResponse({'users': json.loads(data)}, safe=False)

Hay formas de hacerlo con serializadores personalizados solo con campos específicos pero se ha decidido no usarlos en este caso.

## Anotaciones y Comentarios

No sé si la intención de obtener canciones yt artistas favoritos era emplear la llamada a spotify ```https://api.spotify.com/v1/me/tracks```, pero para esta no he sido capaz de realizarla únicamente con código propio o en postman. De actualizar el repo después de escribir esto, añadiré el code la request o una prueba con spotipy para ello.

Hay borrado en cascada para las preferencias si se borra el usuario pero el usuario no tiene ninguna dependencia en el objeto preferencias. Las preferencias no se crean automáticamente con el usuario, sino que solo al añadirle cualquier elemento a una de sus tres categorías.

Al devolver un modelo de django, JsonResponse requiere la etiqueta safe=False.
Si lees esto, mandame un correo con el por qué o apuntalo como si te lo hubiera preguntado en clase para decirlo ahí, y feliz año.

Se crea un super usuario al levantar el proyecto, con variables de entorno en .env. Los detalles de esta operación están en el archivo ejercicio_django/wsgi.py
Leí en docuemntación que era buen lugar para ejecutar parte de las operaciones de inicio, y en los archivos __init__.py no funciona porque los modelos no estñan levantados en db aún.

## ESTRUCTURA DE .ENV
```
export SPOTFY_URI="http://127.0.0.1:8000"
export CLIENT_ID="IDENTIFICADOR"
export CLIENT_SECRET="SECRETO"

export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_PASSWORD="password"
export DJANGO_SUPERUSER_EMAIL="admin@example.com"
export DJANGO_SUPERUSER_FIRST_NAME="john elden ring"
```

## DISCLAIMER

Todos los errores de diseño e implementación de este proyetcoo son fruto del sudor y lagrimas del propietario. Ningun agente de IA ha escrito este código que no llevaré a producción y del cual conozco cada línea. Prefiero conocer mi código a depender de una máquina de alucinaciones entrenada para decir que sí a todo.

La existencia de este disclaimer es fruto del cansancio más honesto.




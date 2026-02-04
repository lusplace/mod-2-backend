"""
WSGI config for ejercicio_django project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/6.0/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ejercicio_django.settings')

application = get_wsgi_application()

from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv
load_dotenv()


ADMIN_USERNAME = os.getenv('DJANGO_SUPERUSER_USERNAME')
ADMIN_PASSWORD = os.getenv('DJANGO_SUPERUSER_PASSWORD')
ADMIN_EMAIL = os.getenv('DJANGO_SUPERUSER_EMAIL')
ADMIN_FIRST_NAME = os.getenv('DJANGO_SUPERUSER_FIRST_NAME')
User = get_user_model()

if not User.objects.filter(username=ADMIN_USERNAME).exists():
    try:
        superuser = User.objects.create_superuser(username = ADMIN_USERNAME, email = ADMIN_EMAIL, password = ADMIN_PASSWORD, first_name= ADMIN_FIRST_NAME)
        print('Superuser created successfully!')
        superuser.save()
    except Exception as e:
        print(f"Exception while creating superUser {e}")
    except ValueError as ve:
        print(f"Value Error while creating super user: {ve}")
else:
    print ('Superuser already exists.')


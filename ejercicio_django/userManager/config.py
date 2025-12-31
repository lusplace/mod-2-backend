from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv
load_dotenv()


ADMIN_USERNAME = os.getenv('ADMIN_USERNAME')
ADMIN_PASSWORD = os.getenv('ADMIN_PASSWORD')
ADMIN_MAIL = os.getenv('ADMIN_MAIL')
ADMIN_MALL = os.getenv('ADMIN_MALL')

User = get_user_model()

if not User.objects.filter(username='admin').exists():
    try:
        print(f"the mall is {ADMIN_MALL}")
        User.objects.create_superuser(ADMIN_USERNAME, ADMIN_MAIL, ADMIN_PASSWORD)
        print('Superuser created successfully!')

    except Exception as e:
        print(e.message)
else:
    print ('Superuser already exists.')
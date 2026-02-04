from django.apps import AppConfig
from django.contrib.auth import get_user_model
import os
from dotenv import load_dotenv

class UsermanagerConfig(AppConfig):
    name = 'userManager'
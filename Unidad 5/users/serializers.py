from rest_framework import serializers
from django.contrib.auth import get_user_model
User = get_user_model()

from django.contrib.auth.models import Group, User
from rest_framework import serializers

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "groups"]


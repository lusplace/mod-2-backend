from .models import Message, ChatRoom
from rest_framework import serializers
from users.serializers import UserSerializer

class ChatRoomSerializer(serializers.ModelSerializer):
    owner = UserSerializer(read_only=True)
    members = UserSerializer(read_only=True, many=True)

    class Meta:
        model = Message
        fields = (
            'room_name',
            'description',
            'owner',
            'members',)

class MessageSerializer(serializers.ModelSerializer):
    chat_room = ChatRoomSerializer(read_only=True)
    owner = UserSerializer(read_only=True)
    author = UserSerializer(read_only=True)

    class Meta:
        model = ChatRoom
        fields = (
            'author',
            'pub_date',
            'body_text',
            'chat_room',
            )
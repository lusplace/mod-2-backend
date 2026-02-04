from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions
from .models import Message, ChatRoom
from .serializers import MessageSerializer, ChatRoomSerializer

class MessageViewSet(viewsets.ModelViewSet):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permissions_classes = [permissions.IsAdminUser]

class ChatRoomViewSet(viewsets.ModelViewSet):
    queryset = ChatRoom.objects.all()
    serializer_class = MessageSerializer
    permissions_classes = [permissions.IsAdminUser]
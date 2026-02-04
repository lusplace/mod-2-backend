from django.shortcuts import render, redirect
from rest_framework import viewsets, permissions, authentication, status
from .models import Message, ChatRoom
from .serializers import MessageSerializer, ChatRoomSerializer

from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Count, Avg

from rest_framework import generics

import logging

logger = logging.getLogger('my_app')

# Create your views here.
#def index(request):
#    return render(request, "chat/index.html")
#
#def room(request, room_name):
#    if not request.user.is_authenticated:
#        return redirect("login-user")
#    return render(request, "chat/room.html", {"room_name": room_name})

class ChatRoomStats(APIView):
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer
    permissions_classes = [permissions.IsAuthenticated]

    def get(self, request):
        #chat_rooms = ChatRoom.objects.all()
        serializer = ChatRoomSerializer
        #conteo_miembros = ChatRoom.objects.annotate(num_miembros=Count('members'))
        #users = User.objects.all()
        chatroom_user_is_owner = ChatRoom.objects.filter(owner=self.request.user)

        return Response(chatroom_user_is_owner)

class ChatRoomListCreateAPIView(generics.ListCreateAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
    queryset = ChatRoom.objects.all()
    serializer_class = MessageSerializer

class ChatRoomRetrieveAPIView(generics.RetrieveAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
    queryset = ChatRoom.objects.all()
    serializer_class = MessageSerializer

class ChatRoomUpdateAPIView(generics.UpdateAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
    queryset = ChatRoom.objects.all()
    serializer_class = ChatRoomSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(owner=user)

    def perform_update(self, serializer):
        instance = serializer.save()

class ChatRoomDestroyAPIView(generics.DestroyAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    
    queryset = ChatRoom.objects.filter()
    serializer_class = ChatRoomSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(owner=user)

    def perform_destroy(self, instance):
        super().perform_destroy(instance)


class MessageListCreateAPIView(generics.ListCreateAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageRetrieveAPIView(generics.RetrieveAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    queryset = Message.objects.all()
    serializer_class = MessageSerializer

class MessageUpdateAPIView(generics.UpdateAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(author=user)

    def perform_update(self, serializer):
        instance = serializer.save()

class MessageDestroyAPIView(generics.DestroyAPIView):
    autentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]
    serializer_class = MessageSerializer

    def get_queryset(self):
        user = self.request.user
        return Message.objects.filter(author=user)
        
    def perform_destroy(self, instance):
        super().perform_destroy(instance)

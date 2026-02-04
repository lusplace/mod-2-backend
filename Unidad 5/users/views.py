from django.shortcuts import render

# Create your views here.
from django.contrib.auth import get_user_model

User = get_user_model()
from django.contrib.auth.models import Group
from rest_framework import permissions, viewsets
from .serializers import UserSerializer
from rest_framework import generics, permissions, authentication, viewsets

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

class UserRegistrationView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({
              "message": "User registered successfully"
            }, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permissions_classes = [permissions.IsAuthenticated]#isAdmin isAuthenticatedOrReadOnly

class UserListCreateAPIView(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]
    permissions_classes = [permissions.IsAuthenticatedOrReadOnly]
  
class UserUpdateAPIView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [authentication.SessionAuthentication]

    def perform_update(self, instance):
        instance = serializer.save()

class UserDestroyAPIView(generics.DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    authentication_classes = [authentication.SessionAuthentication]

    def perform_destroy(self, instance):
        super().perform_destroy(instance)

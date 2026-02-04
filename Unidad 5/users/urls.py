from django.urls import path

from . import views

urlpatterns = [
    path('<int:pk>', views.UserRetrieveAPIView.as_view()),
    path('', views.UserListCreateAPIView.as_view()),   
    path('<int:pk>/update', views.UserUpdateAPIView.as_view()),
    path('<int:pk>/delete', views.UserDestroyAPIView.as_view()),   
]




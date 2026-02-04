from django.urls import include, path
from django.contrib.auth.views import LoginView, LogoutView
from .  import views
from rest_framework.routers import DefaultRouter
from .viewsets import MessageViewSet, ChatRoomViewSet

router = DefaultRouter()

router.register(r'rooms', ChatRoomViewSet)

router.register(r'messages', MessageViewSet)

urlpatterns = [
#    path("", views.index, name="index"),
#    path("<str:room_name>/", views.room, name="room"),
    #path("auth/login/", LoginView.as_view
    #     (template_name="templates/chat/LoginPage.html"), name="login-user"),
    #path("auth/logout/", LogoutView.as_view(), name="logout-user"),
    #path("chat_data/", ChatRoomStats.as_view(), name='chat-stats'),
    path('', include(router.urls)),

    path('room/<int:pk>/stats', views.ChatRoomStats.as_view()),

    path('room/<int:pk>',           views.ChatRoomRetrieveAPIView.as_view()),
    path('room/',                   views.ChatRoomListCreateAPIView.as_view()),
    path('room/<int:pk>/modify',    views.ChatRoomUpdateAPIView.as_view()),
    path('room/<int:pk>/delete',    views.ChatRoomDestroyAPIView.as_view()),

    path('message/<int:pk>',        views.MessageRetrieveAPIView.as_view()),
    path('message/',                views.MessageListCreateAPIView.as_view()),
    path('message/<int:pk>/update', views.MessageUpdateAPIView.as_view()),
    path('message/<int:pk>/delete', views.MessageDestroyAPIView.as_view()),

]



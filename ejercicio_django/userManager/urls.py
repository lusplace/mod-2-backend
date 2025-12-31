from django.urls import include, path
from . import views

# Create your views here.
urlpatterns = [
    path("", views.get_users, name="users"),
    path("username/<str:username>", views.get_user_by_username, name="get_users"),

    path("get", views.get_users, name="get_users"),
    path("add", views.add_user, name="add_user"),
    path("delete/username/<str:username>", views.remove_user, name="delete_user"),
    path("update", views.update_user, name="update_user"),
]

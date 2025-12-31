from django.urls import include, path
from . import views

urlpatterns = [

    path("preferences/add", views.add_preference, name="add"),
    
    path("preferences", views.get_all_preferences, name="prefs"),
    path("preferences/<str:username>", views.get_user_preferences, name="prefs by user"),
    path("preferences/<str:username>/<str:pref_type>", views.get_user_type_preferences, name="prefs by user and type"),

    path("preferences/clear/user/<str:username>/type/<str:pref_type>", views.clear_preference_type, name="delete"),
    path("preferences/clear/user/<str:username>", views.clear_all_preferences, name="delete"),

    path("", views.get_spotify_favourites, name='favs')

]

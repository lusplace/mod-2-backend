from django.urls import include, path
from . import views

urlpatterns = [

    path("preferences/add/<int:user_id>/<str:pref_type>", views.add_preference, name="add"),
    
    path("preferences", views.get_all_preferences, name="prefs"),
    path("preferences/read/<int:user_id>", views.get_user_preferences, name="prefs by user"),
    path("preferences/read/<int:user_id>/<str:pref_type>", views.get_user_type_preferences, name="prefs by user and type"),

    path("preferences/empty/<int:user_id>/<str:pref_type>", views.empty_preference_type, name="delete"),
    path("preferences/empty/<int:user_id>/", views.empty_all_preferences, name="delete"),

    #path("preference/remove/<int:user_id>/<str:pref_type>", views.empty_preference, name="delete"),

]


##
# 
#
#
# #

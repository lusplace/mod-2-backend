from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from .models import Preferences, Track, Album, Artist
from .spotify_connector import get_spotify_object, get_favs
from rest_framework.decorators import api_view
from django.core import serializers
import json

# UTILS
def get_pref_class(pref_type):
    PrefClass = None
    match pref_type:
        case 'track':
            PrefClass = Track
        case 'album':
            PrefClass = Album
        case 'artist':
            PrefClass = Artist
    print(f"choosing prefclass {pref_type}")
    return PrefClass

def get_user_by_username(username):
    print(f"searching user {username}")
    User = get_user_model()

    try:
        user = User.objects.get(username = username)
        return user

    except User.DoesNotExist:
        print(f"User {username} does not exist")    
        return None
    except Exception as e: 
        print(f"Unexpected error with user {username}")    
        return None

def get_prefs(user):
    if(user is None):
        return
    try:
        prefs = Preferences.objects.get(user = user)
    except Preferences.DoesNotExist:
        prefs = Preferences(user = user)
        print(f"Creating preferences for {user}")
        prefs.save()
    except:
        return None
        print("Cant create preferences")
    return prefs

@api_view(['GET'])
# Create your views here.
def api_home(request, *arg, **kwargs):
    return JsonResponse({'message':'Hola mundo preferencias'})

@api_view(['POST'])
def add_preference( request):

    data = json.loads(request.body)
    username = data['username']
    pref_type = data.get('pref_type', 'track')
    spotify_id = data['spotify_id']

    PrefClass = get_pref_class(pref_type)
    print(f"retrieved pref class {PrefClass.__name__}")

    if(PrefClass == None): 
        return JsonResponse({'status':'false','message':f"null preference type, it must be one of song, album or artist"}, status=400)
    
    try:
        print(f"try retrieve spotify object")
        spotify_object = PrefClass.objects.get(spotify_id = spotify_id)

        #spotify_object = PrefClass.objects.get(spotify_id = spotify_id)
        print(f"got object {spotify_object}")

    except:
        print(f"spotify object not found, retrieving new one")
        data = get_spotify_object(spotify_type = f"{pref_type}s", spotify_id = spotify_id)
        spotify_object = PrefClass(name = data['name'], spotify_id = data['spotify_id'])

    try:
        User = get_user_model()
        user = get_user_by_username(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    except:
        return JsonResponse({'status':'false','message': f"Unexpected User error"}, status=400)  

    spotify_object.save()

    if(pref_type =='album'): prefs.albums.add(spotify_object)
    else: 
        if(pref_type =='track'): prefs.tracks.add(spotify_object)
        else: 
            if(pref_type =='artist'): prefs.artists.add(spotify_object)
    prefs.save()
    return JsonResponse({'message':f"{spotify_object} added successfully to {prefs}"}, status=200)

# READ
@api_view(['GET'])
def get_all_preferences(request):
    all_entries = Preferences.objects.all()
    data = serializers.serialize("json", all_entries)

    #json = serializers.serialize("json", users, fields=[ALLOWED_FILTERS, 'id'])
    return JsonResponse({'preferences': json.loads(data)}, safe=False)

@api_view(['GET'])
def get_user_preferences(request, username):
    User = get_user_model()
    try:
        user = get_user_by_username(username)
        print(user)
        prefs = get_prefs(user)
        print(prefs)
        data = serializers.serialize("json", prefs)
        print(data)
        return JsonResponse({'preferences': json.loads(data)}, safe=False)

    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except:
        return JsonResponse({'status':'false','message': f"User {username} is wrong"}, status=400)  

    all_entries = Preferences.objects.get(user = user)

@api_view(['GET'])
def get_user_type_preferences(request, username, pref_type):
    User = get_user_model()
    try:
        user = get_user_by_username(username)
        print(user)
        prefs = get_prefs(user)
        print(prefs)
        data = {}
        if(pref_type =='album'): data = prefs.albums
        elif(pref_type =='track'): data = prefs.tracks
        elif(pref_type =='artist'): data = prefs.artists
        data = serializers.serialize("json", data)
    
        print(data)
        return JsonResponse({'preferences': json.loads(data)}, safe=False)

    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except:
        return JsonResponse({'status':'false','message': f"User {username} is wrong"}, status=400)  

    all_entries = Preferences.objects.get(user = user)

#DELETE
@api_view(['DELETE'])
def clear_preference_type(request, username, pref_type):
    try:
        User = get_user_model()
        user = get_user_by_username(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  

    if(pref_type =='album'): prefs.albums.clear()
    else: 
        if(pref_type =='track'): prefs.tracks.clear()
        else: 
            if(pref_type =='artist'): prefs.artists.clear()
            else:
                return JsonResponse({'message': "wrong preferences"}, status=400)
    prefs.save()
    
    return JsonResponse({'message': f"prefs emptied for type {pref_type}"}, status=200)

@api_view(['DELETE'])
def clear_all_preferences(request, username):
    try:
        User = get_user_model()
        user = get_user_by_username(username)
        prefs = get_prefs(user)
        prefs.albums.clear()
        prefs.artists.clear()
        prefs.tracks.clear()

        prefs.save()
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  

    
    return JsonResponse({'message': f"prefs emptied for {user}"}, status=200)

@api_view(['GET'])
def get_spotify_favourites(request):
    try:
        favs = get_favs()
        data = serializers.serialize("json", favs)

        return JsonResponse({'users': json.loads(data)})
    except:
        return JsonResponse({'message': 'check your spotify credentials'}, status=400)

from django.shortcuts import render
from django.http import JsonResponse
from django.contrib.auth import get_user_model
from . import models
from .spotify_connector import get_spotify_object
from rest_framework.decorators import api_view


def get_user_by_username(username : str):
    User = get_user_model()
    user = User.objects.get(username = username)
    return user

def get_user_by_id(user_id : int):
    User = get_user_model()
    user = User.objects.get(id = user_id)
    return user

def get_prefs(user):
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
def add_preference(user_id:int, pref_type:str, request):
    try:
        PrefClass = get_pref_class(pref_type)
        if(PrefClass == None): 
            return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)
    except:
        return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)

    try:
        spotify_id = request.GET['spotify_id']
        spotify_object = PrefClass.objects.get(spotify_id = spotify_id)
    except PrefClass.DoesNotExist:
        name, spotify_id = get_spotify_object(spotify_type = pref_type, spotify_id = trackId)
        spotify_object = PrefClass(name = name, spotify_id = spotify_id)
    except:
        return JsonResponse({'status':'false','message':f"error retrieving {PrefClass.__name__}"}, status=400)

    try:
        username = request.GET['username']
        user = get_user_by_username(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    
    prefs[f"{pref_type}s"].add(spotify_object)
    prefs.save()
    
    return JsonResponse({'message':f"{pref_type} {spotify_object} added successfully to {prefs}"}, status=200)


# READ
@api_view(['GET'])
def get_all_preferences(request):
    all_entries = Preferences.objects.all()
    return JsonResponse(all_entries, safe=False)

@api_view(['GET'])
def get_user_preferences(user_id, request):
    try:
        user = get_user_by_username(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    
    all_entries = Preferences.objects.get(user = user)

@api_view(['GET'])
def get_user_type_preferences(user_id, pref_type, request):
    try:
        pref_type = request.GET['type'] | 'tracks'
        PrefClass = get_pref_class(pref_type)
        if(PrefClass == None): 
            return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)
    except:
        return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)

    try:
        user = get_user_by_id(user_id)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    
    return JsonResponse({'message': prefs}, status=200, safe=False)

#DELETE
@api_view(['DELETE'])
def empty_preference_type(request, user_id, pref_type):

    try:
        pref_type = request.GET['type'] | 'tracks'
        PrefClass = get_pref_class(pref_type)
        if(PrefClass == None): 
            return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)
    except:
        return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)

    try:
        username = request.GET['username']
        user = get_user_by_username(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    
    prefs[f"{pref_type}s"].empty()
    prefs.save()
    
    return JsonResponse({'message': "prefs emptied"}, status=200)

@api_view(['DELETE'])
def empty_all_preferences(request, user_id):
    try:
        pref_type = request.GET['type'] | 'tracks'
        PrefClass = get_pref_class(pref_type)
        if(PrefClass == None): 
            return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)
    except:
        return JsonResponse({'status':'false','message':f"wrong preference type, it must be one of song, album and artist"}, status=400)

    try:
        user = get_user_by_id(username)
        prefs = get_prefs(user)
    except User.DoesNotExist:
        return JsonResponse({'status':'false','message': f"User {username} does not exist"}, status=400)  
    except Model.MultipleObjectsReturned as e: 
        return JsonResponse({'status':'false','message': f"Multiple users with {username} as username "}, status=400)  
    
    prefs["albums"].empty()
    prefs["artists"].empty()
    prefs["songs"].empty()

    prefs.save()
    
    return JsonResponse({'message': f"prefs emptied for {user}"}, status=200)

# UTILS
def get_pref_class(pref_type):
    PrefClass = None
    match pref_type:
        case 'song':
            PrefClass = Song
        case 'track':
            PrefClass = Song
        case 'album':
            PrefClass = Album
        case 'artist':
            PrefClass = Artist
    return PrefClass

from django.shortcuts import render
from django.contrib.auth import get_user_model
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.http import JsonResponse
from django.core import serializers
import json

ALLOWED_FILTERS = ['username', 'email', 'first_name', 'last_name']

# CREATE
@api_view(['POST'])
def add_user(request):
    try:
        data = json.loads(request.body)
        username = data['username']
        first_name = data['first_name']
        last_name = data.get('last_name', '')
        email = data['email']
        password = data['password']
        phone_number = data.get('phone_number', 0)
    except:
        print("Parameter error")

    try:
        User = get_user_model()

        user = User(
            username = username, 
            first_name = first_name, 
            last_name = last_name,
            email = email, 
            password = password, 
            phone_number = phone_number
            )
        #user.save()
        print("good so far")
        user.save()
        print("user saved!")
        
        return JsonResponse({"message": f"user created successfully"}, safe=False)
    except:
        print("Error creating user")

    return JsonResponse({'error': "bad request"}, status=404)

# READ MANY
@api_view(['GET'])
def get_users(request, *arg, **kwargs):
    User = get_user_model()
    users = User.objects.all()
  
    users = User.objects.filter(
        username__icontains = request.GET.get('username', ''),
        first_name__icontains = request.GET.get('first_name', ''),
        last_name__icontains = request.GET.get('last_name', ''),
        email__icontains = request.GET.get('email', '') 
    )
    data = serializers.serialize("json", users)

    return JsonResponse({'users': json.loads(data)}, safe=False)

@api_view(['GET'])
def get_user_by_username(request, username, *arg, **kwargs):
    User = get_user_model()

    try:
        user = User.objects.get(username = username)

        if username is None:
            return JsonResponse({'status':'false','message':'no username provided'}, status=400, safe=False)
    
        return JsonResponse({'status':'true','message':str(user)}, status=200, safe=False)

    except User.DoesNotExist:
        return JsonResponse({'status':'false','message':"user doesnt exist, check spelling"}, status=404, safe=False)

    except Exception as e: 
        return JsonResponse({'status':'false','message':f"error accessing db"}, status=401, safe=False)

    return JsonResponse({'status':'false','message':f"error"}, status=401, safe=False)

# UPDATE
@api_view(['PUT', 'PATCH'])
def update_user(request):

    try:
        data = json.loads(request.body)
        username = data['username']
        first_name = data('first_name', None)
        last_name = data.get('last_name', None)
        email = data('email', None)
        password = data('password', None)
        phone_number = data.get('phone_number', None)
    except:
        print("Parameter error")

    try:
        User = get_user_model()
        print(f"username is {username}")
        u = User.objects.get(username = username)
        for key in data:
            if key in data and key is not None and key in ALLOWED_FILTERS:
                setattr(u, key, data[key])
        u.save()
        return JsonResponse({"message": f"User {username} updated"}, status=200)

    except User.DoesNotExist:
        return JsonResponse({"message": "User does not exist"}, status=404)

    except Exception as e: 
        return JsonResponse({"message": f"Error accesssing DB: {e}"}, safe=False, status=400)

    return JsonResponse({"ERROR": "Contact System administrator"}, safe=False)

# DELETE
@api_view(['DELETE'])
def remove_user(request, username):
    User = get_user_model()

    try:
        u = User.objects.get(username = username)
        u.delete()
        return JsonResponse({"message": f"User {username} deleted"}, status=200)

    except User.DoesNotExist:
        return JsonResponse({"message": "User does not exist"}, status=404)

    except Exception as e: 
        return JsonResponse({"message": f"Error accesssing DB: {e}"}, safe=False, status=400)


    return JsonResponse({"UserDeleted": str(u)}, safe=False)
    

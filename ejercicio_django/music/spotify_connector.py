import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
load_dotenv()

SPOTFY_URI = os.getenv('SPOTFY_URI')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')
SCOPE = 'user-library-read'
access_token = ''
expiration_date = datetime.now()


def get_token() -> {str, datetime}:
    global access_token
    global expiration_date
    if datetime.now() < expiration_date: 
        print("dont need new access_token")
        return
    url = "https://accounts.spotify.com/api/token"

    payload = f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&scope={SCOPE}"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = (json.loads(response.text))['access_token']
    expiration_date = datetime.now() + timedelta(hours=1)
    return 

def get_spotify_object(spotify_type : str, spotify_id : str):
    global access_token
    global expiration_date
    print(f"entered spotify object getter {access_token}")
    get_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    #print(f"access token is : {access_token}")
    url = f"https://api.spotify.com/v1/{spotify_type}/{spotify_id}"
    response = requests.request("GET", url, headers=headers)
    response = (json.loads(response.text))

    try:
        return {
            'name': response['name'], 
            'spotify_id': response['id']}
    except:
        return response

def get_favs():
    global access_token
    global expiration_date
    get_token()
    print(expiration_date)
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    #print(f"access token is : {access_token}")
    url = f"https://api.spotify.com/v1/me/tracks"
    response = requests.request("GET", url, headers=headers)
    print(response.text)
    return response.text




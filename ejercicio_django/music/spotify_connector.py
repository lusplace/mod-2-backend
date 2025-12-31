import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
import base64

load_dotenv()

SPOTFY_URI = f"{os.getenv('SPOTIFY_URI')}/callback"
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

SCOPE = 'user-library-read user-read-private user-read-email'
access_token = ''
expiration_date = datetime.now()
encoded_credentials = base64.b64encode(CLIENT_ID.encode() + b':' + CLIENT_SECRET.encode()).decode("utf-8")

token_headers = {
    "Authorization": "Basic " + encoded_credentials,
    'Content-Type': 'application/x-www-form-urlencoded',
    'scope': SCOPE,
    "response_type": "code"
    #"code_challenge_method": "S256",
    #"code_challenge": challenge
    }

def get_token():
    global access_token
    global expiration_date

    if datetime.now() < expiration_date: 
        print("dont need new access_token")
        return
    url = "https://accounts.spotify.com/api/token"

    #payload = f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}&scope={SCOPE}"
    #headers = {
    #'Content-Type': 'application/x-www-form-urlencoded',
    #}

    token_data = {
        "grant_type": "client_credentials",
        "code": "code",
        "redirect_uri": SPOTFY_URI,
        "scope": SCOPE

    }

    response = requests.request("POST", url, headers=token_headers, data=token_data)
    print(response.text)
    access_token = (json.loads(response.text))['access_token']
    expiration_date = datetime.now() + timedelta(hours=1)
    return 

get_token()

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




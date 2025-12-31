import requests
import os
from dotenv import load_dotenv
from datetime import datetime, timedelta
import json
load_dotenv()

SPOTFY_URI = os.getenv('SPOTFY_URI')
CLIENT_ID = os.getenv('CLIENT_ID')
CLIENT_SECRET = os.getenv('CLIENT_SECRET')

def get_token() -> {str, datetime}:

    url = "https://accounts.spotify.com/api/token"

    payload = f"grant_type=client_credentials&client_id={CLIENT_ID}&client_secret={CLIENT_SECRET}"
    headers = {
    'Content-Type': 'application/x-www-form-urlencoded',
    }

    response = requests.request("POST", url, headers=headers, data=payload)
    access_token = (json.loads(response.text))['access_token']
    expiration_date = datetime.now() + timedelta(hours=1)
    return {access_token, expiration_date}
    
def get_spotify_object(spotify_type : str, spotify_id : str):
    if datetime.now() >= expiration_date: 
        access_token, expiration_date = get_new_token()
    headers = {
        'Authorization': f'Bearer {access_token}',
    }
    url = f"https://api.spotify.com/v1/{spotify_type}/{spotify_id}"
    response = requests.request("GET", url, headers=headers)
    response = (json.loads(response.text))
    return {name: response['name'], spotify_id: response['id']}

access_token, expiration_date = get_token()


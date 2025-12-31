# https://docs.djangoproject.com/en/6.0/ref/contrib/auth/
# Create your models here.
from django.db import models
from userManager.models import CustomUser as User

spotifyBaseLink = 'https://api.spotify.com/v1/'

class SpotifyObject(models.Model):
    name = models.CharField(max_length=30, default='')
    spotify_id = models.CharField(max_length=30, unique=True)
    REQUIRED_FIELDS = ['spotify_id', 'name']
    
    def __str__(self):
        return f"{self.name}"

    def url(self):
        return ""

class Track(SpotifyObject):
    def link(self):
        return f"{spotifyBaseLink}track/{self.spotify_id}"

    def __str__(self):
        return f"Track: {self.name}"
    
    def url(self):
        return f"https://api.spotify.com/v1/tracks/{self.spotify_id}"

class Artist(SpotifyObject):
    def link(self):
        return f"{spotifyBaseLink}artist/{self.spotify_id}"

    def __str__(self):
        return f"Artist: {self.name}"

    def url(self):
        return f"https://api.spotify.com/v1/tracks/{self.spotify_id}"

class Album(SpotifyObject):
    def link(self):
        return f"{spotifyBaseLink}album/{self.spotify_id}"

    def __str__(self):
        return f"Album: {self.name}"

    def url(self):
        return f"https://api.spotify.com/v1/tracks/{self.spotify_id}"

class Preferences(models.Model):
    # Automatically sets the creation date
    created_at = models.DateTimeField(auto_now_add=True)
    
    # Automatically updates the field on each save
    updated_at = models.DateTimeField(auto_now=True)

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    tracks = models.ManyToManyField(Track, blank=True)
    artists = models.ManyToManyField(Artist, blank=True)
    albums = models.ManyToManyField(Album, blank=True)

    def __str__(self):
        return f"{self.user.username}'s preferences"




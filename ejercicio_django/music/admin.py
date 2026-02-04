from django.contrib import admin
from .models import Track, Artist, Album, Preferences

# Register your models here.

class TrackAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']
class ArtistAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']
class AlbumAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']

class PreferencesAdmin(admin.ModelAdmin):
    fields = ['user', 'tracks', 'artists', 'albums']

admin.site.register(Track, TrackAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Preferences, PreferencesAdmin)

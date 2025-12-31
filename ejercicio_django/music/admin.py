from django.contrib import admin
from .models import Song, Artist, Album, Preferences

# Register your models here.

class SongAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']
class ArtistAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']
class AlbumAdmin(admin.ModelAdmin):
    fields = ['spotify_id', 'name']

class PreferencesAdmin(admin.ModelAdmin):
    fields = ['user', 'songs', 'artists', 'albums']

admin.site.register(Song, SongAdmin)
admin.site.register(Artist, ArtistAdmin)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Preferences, PreferencesAdmin)

from django.shortcuts import render
from django.http.response import HttpResponse
import spotipy
import spotipy.util as util
from models import Playlist

playlist_id = "4qD4DebVGI5VZwRV0bcZ66"

steve_spotify_id = '1210159879'

trevor_spotify_id = "123004043"

# Create your views here.
def index(request):
    playlists = Playlist.objects.all()
    return HttpResponse(str([p.name for p in playlists]))

def seed(request):
    token = util.prompt_for_user_token(steve_spotify_id, 'playlist-modify-public')

    sp = spotipy.Spotify(token)
    playlists = sp.user_playlists(steve_spotify_id, limit=50)['items']
    for p in playlists:
        print p
        Playlist.objects.create(spotify_id=p['id'], user_id=steve_spotify_id, name=p['name'])
    return HttpResponse("seeded with steves playlists")

import sys
import spotipy
import spotipy.util as util
from collections import Counter
from collections import defaultdict

def getPlaylistGenres(uname, pid):

    artistsDict = defaultdict(lambda: '')
    artistsNumAppearances = []
    genres = []
    results = sp.user_playlist_tracks(uname, playlist_id=pid)
    for item in results['items']:
        for artist in item['track']['artists']:
            artistsDict[artist['name']] = artist['id']
            artistsNumAppearances.append(artist['name'])
    artistsNumAppearances = Counter(artistsNumAppearances)

    for aName, _ in artistsNumAppearances.most_common(10):
        artistInfo = sp.artist(artistsDict[aName])
        for genre in artistInfo['genres']:
            genres.append(genre)
    genreCount = Counter(genres)
    return genreCount

scope = ''

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print "Usage: %s username" % (sys.argv[0],)
    sys.exit()

token = util.prompt_for_user_token(username, scope)

if token:

    sp = spotipy.Spotify(auth=token)
    playlistId = '4qD4DebVGI5VZwRV0bcZ66'
    print getPlaylistGenres(username, playlistId)


else:
    print "Can't get token for", username
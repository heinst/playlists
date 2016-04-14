import sys
import spotipy
import spotipy.util as util


def get_playlist_length(uname, pid):

    durations = []
    results = sp.user_playlist_tracks(uname, playlist_id=pid)
    for item in results['items']:
        durations.append(item['track']['duration_ms'])
    msTotal = sum(durations)
    x = msTotal / 1000
    seconds = x % 60
    x /= 60
    minutes = x % 60
    x /= 60
    hours = x % 24
    x /= 24

    return "{0:02d}:{1:02d}:{2:02d}".format(hours, minutes, seconds)

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
    print get_playlist_length(username, playlistId)


else:
    print "Can't get token for", username
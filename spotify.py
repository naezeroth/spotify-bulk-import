import sys
import spotipy
import spotipy.util as util
from tinytag import TinyTag
import os
from os.path import join, dirname
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

client_id = os.getenv('SPOTIPY_CLIENT_ID')
client_secret = os.getenv('SPOTIPY_CLIENT_SECRET')
playlist = os.getenv('PLAYLIST')

scope = 'playlist-modify-public'

def getInfo(path):
    mp3 = TinyTag.get(path)
    toReturn = []
    toReturn.append(mp3.artist)
    toReturn.append(mp3.title)
    return toReturn

if len(sys.argv) > 1:
    username = sys.argv[1]
else:
    print("Usage: %s username" % (sys.argv[0]))
    sys.exit()
        
token = util.prompt_for_user_token(username,scope,client_id,client_secret,redirect_uri='http://localhost/') 

if token:
    sp = spotipy.Spotify(token)
    names = os.listdir(os.getcwd())
    for n in names:
        if(n.lower().endswith(('.mp3', '.m4a', '.wav', '.wma', '.ogg', '.mp4', '.m4b'))):
            try:
                artistName = getInfo(n)[0]
                trackName = getInfo(n)[1]
                q = "artist:%s track:%s"%(artistName, trackName)
                if(artistName != None and trackName != None):
                    result = sp.search(q, type="track", limit=1)
                    track_id = result.get('tracks').get('items')[0].get('id')
                    results = sp.user_playlist_add_tracks(username, playlist, [track_id])   
                    print("Successfully added %s by %s to your playlist"%(trackName, artistName))
                continue
            except:
                continue
else:
    print("Can't get token for", username)

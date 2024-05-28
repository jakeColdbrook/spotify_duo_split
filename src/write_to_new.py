import pandas as pd
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
import os

load_dotenv()

# Load the environment variables for the accounts
client_id_NEW = os.getenv('SPOTIFY_CLIENT_ID_NEW')
client_secret_NEW = os.getenv('SPOTIFY_CLIENT_SECRET_NEW')
redirect_uri_NEW = os.getenv('SPOTIFY_REDIRECT_URI_NEW')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id_NEW,
                                               client_secret=client_secret_NEW,
                                               redirect_uri=redirect_uri_NEW,
                                               scope='playlist-modify-public user-follow-modify user-library-modify',
                                               cache_path=None))


##################### Playlists #####################
df_playlists = pd.read_csv('spotify_playlists.csv')

for index, row in df_playlists.iterrows():
    if row['owner'] == 'julie_bkk':
        sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id_2, client_secret=client_secret_2, redirect_uri=redirect_uri_2, scope='playlist-modify-public'))

        playlist_url = row['url']
        playlist_id = playlist_url.split('/')[-1]

        tracks = []
        results = sp.playlist_tracks(playlist_id)
        while results:
            tracks.extend(results['items'])
            if results['next']:
                results = sp.next(results)
            else:
                results = None

        track_ids = [track['track']['id'] for track in tracks]

        playlist = sp.user_playlist_create(user='julie_bkk', name=row['name'])

        sp.playlist_add_items(playlist_id=playlist['id'], items=track_ids)

##################### Artists #####################
df_artists = pd.read_csv('spotify_artists.csv')

for index, row in df_artists.iterrows():
    if row['owner'] == 'new_account':
        artist_url = row['url']
        artist_id = artist_url.split('/')[-1]

        sp.user_follow_artists(ids=[artist_id])

##################### Albums #####################
df_albums = pd.read_csv('spotify_albums.csv')

for index, row in df_albums.iterrows():
    if row['owner'] == 'new_account':
        album_url = row['url']
        album_id = album_url.split('/')[-1]

        sp.current_user_saved_albums_add(albums=[album_id])

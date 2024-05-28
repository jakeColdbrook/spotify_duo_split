from dotenv import load_dotenv
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import pandas as pd

load_dotenv()

client_id = os.getenv('SPOTIFY_CLIENT_ID_OLD')
client_secret = os.getenv('SPOTIFY_CLIENT_SECRET_OLD')
redirect_uri = os.getenv('SPOTIFY_REDIRECT_URI_OLD')

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=client_id,
                                               client_secret=client_secret,
                                               redirect_uri=redirect_uri,
                                               scope='playlist-modify-public playlist-modify-private user-follow-modify user-library-modify',
                                               cache_path=None))

##################### Playlists #####################
df_playlists = pd.read_csv('spotify_playlists.csv')

for index, row in df_playlists.iterrows():
    if row['owner'] == 'new_account':
        playlist_url = row['url']
        playlist_id = playlist_url.split('/')[-1]

        sp.user_playlist_unfollow(user='new_account', playlist_id=playlist_id)

##################### Artists #####################
df_artists = pd.read_csv('spotify_artists.csv')

for index, row in df_artists.iterrows():
    if row['owner'] == 'new_account':
        artist_url = row['url']
        artist_id = artist_url.split('/')[-1]

        sp.user_unfollow_artists(ids=[artist_id])

df_albums = pd.read_csv('spotify_albums.csv')

##################### Albums #####################
for index, row in df_albums.iterrows():
    if row['owner'] == 'new_account':
        album_url = row['url']
        album_id = album_url.split('/')[-1]

        sp.current_user_saved_albums_delete(albums=[album_id])

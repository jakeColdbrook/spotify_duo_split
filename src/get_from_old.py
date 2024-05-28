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
                                               scope='playlist-read-private user-follow-read user-library-read',
                                               cache_path=None))


##################### Playlists #####################
playlists = sp.current_user_playlists()

df_playlists = pd.DataFrame(columns=['name', 'description', 'url', 'owner'])


for playlist in playlists['items']:
    new_row = pd.DataFrame({'name': [playlist['name']], 'description': [playlist['description']], 'url': [playlist['external_urls']['spotify']], 'owner': ['your_spotify_username']})
    df_playlists = pd.concat([df_playlists, new_row], ignore_index=True)

df_playlists.to_csv('spotify_playlists.csv', index=False)


##################### Artists #####################
followed_artists = sp.current_user_followed_artists()

df_artists = pd.DataFrame(columns=['name', 'url', 'owner'])

for artist in followed_artists['artists']['items']:
    new_row = pd.DataFrame({'name': [artist['name']], 'url': [artist['external_urls']['spotify']], 'owner': ['your_spotify_username']})
    df_artists = pd.concat([df_artists, new_row], ignore_index=True)

df_artists.to_csv('spotify_artists.csv', index=False)

##################### Albums #####################
saved_albums = sp.current_user_saved_albums()

df_albums = pd.DataFrame(columns=['name', 'url', 'owner'])

for album in saved_albums['items']:
    new_row = pd.DataFrame({'name': [album['album']['name']], 'url': [album['album']['external_urls']['spotify']], 'owner': ['your_spotify_username']})
    df_albums = pd.concat([df_albums, new_row], ignore_index=True)

df_albums.to_csv('spotify_albums.csv', index=False)
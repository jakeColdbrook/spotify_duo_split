# Spotify-duo-split
I created this to help my wife and I split an old shared spotify 
account into 2 separate account using spotify duo. It does the following:
1. Creates files with all playlists, albums, and artists on the old account.
2. Allows you to assign which account they should be on after the split.
3. Adds all the designated music to the new account.
4. Removes everything sent to the new account from the old account.

# Instructions

1. Install libraries using `pip install -r requirements.txt`
2. Go to developer.spotify.com and create a new App for each account.
3. Create .env file with the client_id and client_secret for each account.
**Example**
```
SPOTIFY_CLIENT_ID_OLD=''
SPOTIFY_CLIENT_SECRET_OLD=''
SPOTIFY_REDIRECT_URI_OLD='http://localhost:8000'

SPOTIFY_CLIENT_ID_NEW=''
SPOTIFY_CLIENT_SECRET_NEW=''
SPOTIFY_REDIRECT_URI_NEW='http://localhost:8000'
```
4. Execute `get_from_old.py`. This will open a browser window and prompt you to log in. Ensure it's loading the correct 
account. Next, it will create the following .csv files:
   * spotify_albums.csv
   * spotify_artists.csv
   * spotify_playlists.csv

5. Open each .csv file and set the `owner` column to either `old_account` or `new_account`.
6. Log out of the old account in the browser.
7. Execute `write_to_new.py`. It will prompt you to log into an account. Log into the account you want to move 
information to.
8. Log out of the new account in the browser.
9. Execute `remove_from_old.py`. Again, it will prompt you to log into an account. Log back into the old account.


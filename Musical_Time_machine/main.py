import os
import spotipy
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from spotipy.oauth2 import SpotifyOAuth

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
SPOTIFY_USERNAME = os.getenv("USERNAME")
SPOTIFY_CLIENT_ID = os.getenv("SPOTIPY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = os.getenv("SPOTIPY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = os.getenv("SPOTIPY_REDIRECT_URI")

"""
    This program is supposed to:
        a. Take a date from within the past 20 years,
        b. Find the billboard 100 from the week of that date,
        c. Scrape and list of songs from Billboard,
        d. Create a playlist of the songs from that week using the Spotify API.
    But Billboard has implemented a paywall that prevents us from scraping the top 100 songs from any other day except the current.
    Therefore our program will:
        a. Scrape billboard.com/charts/hot-100 for the top 100 of the current day.
        b. Create a spotify playlist using the date and the playlist name.
"""
"""---------------------------- GET THE BILLBOARD HOT 100 FOR THE CURRENT WEEK-------------------------------------- """
header = {
    "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/145.0.0.0 Safari/537.36"
}

date = datetime.now().strftime("%Y-%m-%d")

response = requests.get(BILLBOARD_URL, headers=header)
soup = BeautifulSoup(response.text, "html.parser")
title_tags = soup.select(selector="li > #title-of-a-story")

titles_list = [title.getText().strip() for title in title_tags]


"""------------------------------------------ CREATE A PLAYLIST USING THE SONGS IN THE LIST ---------------------------------------"""
scope = "playlist-modify-private"
body = {"name": f"{date}", "public": "false"}

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(client_id=SPOTIFY_CLIENT_ID,
    client_secret=SPOTIFY_CLIENT_SECRET,
    redirect_uri=SPOTIFY_REDIRECT_URI,
    scope=scope
))
current_user = sp.current_user()
user_id = current_user["id"]
print(user_id)
playlist = sp.user_playlist_create(user_id, date, public=False)
print(playlist)


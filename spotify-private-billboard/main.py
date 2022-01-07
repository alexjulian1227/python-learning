import spotipy
from spotipy.oauth2 import SpotifyOAuth
from bs4 import BeautifulSoup
import requests


SPOTIFY_CLIENT_ID = "6d2efd80104d46ee83f4c010926f9677"
SPOTIFY_CLIENT_SECRET = "0290a8f1f82f4853b436f11ba0a3d63a"

sp = spotipy.Spotify(
    auth_manager=SpotifyOAuth(
        scope="playlist-modify-private",
        redirect_uri="https://example.com/callback",
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        show_dialog=True,
        cache_path="token.txt"
    )
)
user_id = sp.current_user()["id"]
print(user_id)

user_year = input("Which year do you want to travel to? Type the date in this format YYYY-MM-DD: ")

main_link = "https://www.billboard.com/charts/hot-100/"
user_link = f"{main_link}{user_year}"

response = requests.get(url=user_link)

soup = BeautifulSoup(response.text, 'html.parser')

all_songs = []
for x in range(0, 100):
    parse_1 = soup.find_all(class_='o-chart-results-list-row-container')[x].h3.string
    all_songs.append(parse_1)
    print(f'Compiling Top {x + 1} song')

song_uris = []

year = user_year.split("-")[0]

for song in all_songs:
    result = sp.search(q=f"track:{song} year:{year}", type="track")
    print(result)
    try:
        uri = result["tracks"]["items"][0]["uri"]
        song_uris.append(uri)
    except IndexError:
        print(f"{song} doesn't exist in Spotify. Skipped.")


playlist = sp.user_playlist_create(user=user_id, name=f"{user_year} Billboard 100", public=False)
print(playlist)

sp.user_playlist_add_tracks(user=user_id, playlist_id=playlist["id"], tracks=song_uris)

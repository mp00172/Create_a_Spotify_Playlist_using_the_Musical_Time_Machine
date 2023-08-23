import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

SPOTIPY_CLIENT_ID = "faf96877ff4c436286b917f158fc2362"
SPOTIPY_CLIENT_SECRET = "552655fb2aa048c5b5a7bd8d9eec3549"
DEFAULT_COUNTRY = "US"


class Spotify:

	def __init__(self):
		self.client_id = SPOTIPY_CLIENT_ID
		self.client_secret = SPOTIPY_CLIENT_SECRET
		self.spotify = None
		self.hot100_search_results = []

	def authenticate(self):
		self.spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(
			client_id=self.client_id,
			client_secret=self.client_secret))

	def TEMPget_artist_top10(self, artist_uri):
		results = self.spotify.artist_top_tracks(artist_id=artist_uri, country=DEFAULT_COUNTRY)
		print(results)

	def format_artist(self, art):
		art = art.lower()
		if "featuring" in art:
			art = art.split("featuring")
			art_formatted = ""
			for i in art:
				art_formatted += str(i)
			return art_formatted
		return art

	def search_for_song(self, no_on_billboard, artist, track_name):
		result = self.spotify.search(q="track:{} artist:{}".format(track_name, self.format_artist(artist)),
									 type="track",
									 limit=1)
		result["number_on_current_billboard"] = no_on_billboard
		result["artist_scraped_from_billboard"] = artist
		result["track_name_scraped_from_billboard"] = track_name
		return result

	def make_hot100_search(self, hot100_scraped):
		for song in hot100_scraped:
			self.hot100_search_results.append(self.search_for_song(no_on_billboard=song[0],
																   artist=song[1],
																   track_name=song[2]))

	def reset_hot100_search_results(self):
		self.hot100_search_results = []

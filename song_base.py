import tkinter as tk
from tkinter import ttk

class Song:
	def __init__(self):
		self.artist = ""
		self.title = ""
		self.spotify_artist_uri = ""
		self.spotify_song_uri = ""
		self.present_on_current_hot100_list = False
		self.number_on_current_hot100_list = None
		self.available_on_spotify = False
		self.add_button = None


class SongBase:
	def __init__(self):
		self.songbase = []

	def song_available_on_spotify(self, song):
		if len(song["tracks"]["items"]) != 0:
			return True
		return False

	def add_hot100(self, spotify_hot100_search_results):
		for entry in spotify_hot100_search_results:
			print(entry)
			song = Song()
			song.present_on_current_hot100_list = True
			song.number_on_current_hot100_list = entry["number_on_current_billboard"]
			if self.song_available_on_spotify(entry):
				song.artist = entry["tracks"]["items"][0]["artists"][0]["name"]
				song.title = entry["tracks"]["items"][0]["name"]
				song.spotify_artist_uri = entry["tracks"]["items"][0]["artists"][0]["uri"]
				song.spotify_song_uri = entry["tracks"]["items"][0]["uri"]
				song.available_on_spotify = True
			else:
				song.artist = entry["artist_scraped_from_billboard"]
				song.title = entry["track_name_scraped_from_billboard"]
			self.songbase.append(song)

	# def add_hot100(self, spotify_hot100_search_results):
	# 	for entry in spotify_hot100_search_results:
	# 		if self.song_available_on_spotify(entry):
	# 			song = Song()
	# 			song.artist = entry["tracks"]["items"][0]["artists"][0]["name"]
	# 			song.title = entry["tracks"]["items"][0]["name"]
	# 			song.spotify_artist_uri = entry["tracks"]["items"][0]["artists"][0]["uri"]
	# 			song.spotify_song_uri = entry["tracks"]["items"][0]["uri"]
	# 			song.present_on_current_hot100_list = True
	# 			song.number_on_current_hot100_list = spotify_hot100_search_results[entry][0]
				# self.songbase.append(song)

	def reset_songbase(self):
		self.songbase = []

	def generate_add_buttons(self):
		self.add_button = ttk.Button

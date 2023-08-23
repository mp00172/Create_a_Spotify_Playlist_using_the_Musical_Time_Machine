import requests

BILLBOARD_URL = "https://www.billboard.com/charts/hot-100/"
BILLBOARD_COMMUNICATION_ERROR_MESSAGE = "There was an error fetching www.billboard.com webpage."
BILLBOARD_WEBPAGE_FETCHED_MESSAGE = "www.billboard.com webpage successfully fetched."


class BillboardFetcher:
	def __init__(self):
		self.webpage = None

	def billboard_status_code_ok(self, sc):
		if sc == 200:
			return True
		return False

	def billboard_webpage_fetching_successful_notification(self):
		print(BILLBOARD_WEBPAGE_FETCHED_MESSAGE)

	def billboard_webpage_fetching_failed_notification(self):
		print(BILLBOARD_COMMUNICATION_ERROR_MESSAGE)

	def get_billboard_webpage(self, date):
		"""Date has to be str, formatted 'YYYY-MM-DD'.
		Year can be provided as any number. Page will return a date between 1952 (or so) and today's date.
		Month cannot be a number larger than 12.
		Day cannot be a number larger than 31."""
		response = requests.get(BILLBOARD_URL + date)
		if self.billboard_status_code_ok(response.status_code):
			self.webpage = response.text
			self.billboard_webpage_fetching_successful_notification()
		else:
			self.billboard_webpage_fetching_failed_notification()

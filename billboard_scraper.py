from bs4 import BeautifulSoup

WEEK_OF_HOT_100_CLASS = "c-tagline  a-font-primary-medium-xs u-font-size-11@mobile-max u-letter-spacing-0106 u-letter-spacing-0089@mobile-max lrv-u-line-height-copy lrv-u-text-transform-uppercase lrv-u-margin-a-00 lrv-u-padding-l-075 lrv-u-padding-l-00@mobile-max"


class BillboardScraper:

	def __init__(self):
		self.raw_html = None
		self.soup = None
		self.results_week_raw = None
		self.week_of_hot_100_formatted = None
		self.titles_raw = []
		self.artists_raw = []
		self.titles_formatted = []
		self.artists_formatted = []
		self.hot_100_formatted = []

	def make_soup(self):
		self.soup = BeautifulSoup(self.raw_html, "html.parser")

	def scrape_week_of_hot_100(self):
		ret = self.soup.select(selector="div div div div div div p")
		ind = 0
		for i in ret:
			ind += 1
			if "Week of" in i.getText():
				self.week_of_hot_100_formatted = i.getText()
				break

	def scrape_titles_raw(self):
		self.titles_raw = self.soup.select(selector="li ul li h3")
		# print(self.titles_raw)
		# print(len(self.titles_raw))

	def scrape_artists_raw(self):
		self.artists_raw = [title.next_sibling.next_sibling for title in self.titles_raw]
		# print(self.artists_raw)
		# print(len(self.artists_raw))

	def format_titles(self):
		self.titles_formatted = [(title_raw.getText()).strip() for title_raw in self.titles_raw]

	def format_artists(self):
		self.artists_formatted = [(artist_raw.getText()).strip() for artist_raw in self.artists_raw]

	def format_hot_100(self):
		self.hot_100_formatted = [(i + 1, self.artists_formatted[i], self.titles_formatted[i]) for i in range(len(self.artists_formatted))]

	def scrape_and_format_hot_100(self):
		self.scrape_titles_raw()
		self.scrape_artists_raw()
		self.format_titles()
		self.format_artists()
		self.format_hot_100()




	def reset_raw_html(self):
		self.raw_html = None

	def reset_titles_raw(self):
		self.titles_raw = []

	def reset_artists_raw(self):
		self.artists_raw = []

	def reset_titles_formatted(self):
		self.titles_formatted = []

	def reset_artists_formatted(self):
		self.artists_formatted = []

	def reset_hot_100_formatted(self):
		self.hot_100_formatted = []

	def reset_results_week_raw(self):
		self.results_week_raw = None

	def reset_week_of_hot_100_formatted(self):
		self.week_of_hot_100_formatted = None



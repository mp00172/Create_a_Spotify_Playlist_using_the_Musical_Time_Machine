import tkinter as tk
from tkinter import ttk
import config
import datetime
from PIL import Image
from PIL import ImageTk
from billboard_fetcher import BillboardFetcher
from billboard_scraper import BillboardScraper
from spotify import Spotify

YEAR_TODAY = int(str(datetime.datetime.now()).split()[0].split("-")[0])

billboard_fetcher = BillboardFetcher()
billboard_scraper = BillboardScraper()
spotify = Spotify()


class Gui:
    def __init__(self):
        self.main_window = None
        self.labelframe_upper = None
        self.spinbox_day_value = None
        self.spinbox_month_value = None
        self.spinbox_year_value = None
        self.spinbox_day = None
        self.spinbox_month = None
        self.spinbox_year = None
        self.labelframe_upper_spacer = None
        self.scrape_billboard_button = None
        self.help_button_image = None
        self.help_button = None
        self.date_for_scraping = ""
        self.date_entry_not_valid_window = None

    def authenticate_with_spotify(self):
        spotify.authenticate()

    def create_main_window(self, size, title):
        self.main_window = tk.Tk()
        self.main_window.geometry(size)
        self.main_window.resizable(False, False)
        self.main_window.title(title)

    def create_labelframe_upper(self):
        self.labelframe_upper = ttk.Labelframe(
            self.main_window,
            text=config.LABELFRAME_UPPER_TEXT,
            width=config.LABELFRAME_UPPER_SIZE["width"],
            height=config.LABELFRAME_UPPER_SIZE["height"]
        )
        self.labelframe_upper.grid(
            row=0,
            column=0,
            padx=10,
            pady=10,
            columnspan=2,
            sticky="N"
        )

    def fill_labelframme_upper(self):
        self.create_spinboxes()
        self.create_labelframe_upper_spacer()
        self.create_scrape_billboard_button()
        self.create_help_button_image()
        self.create_help_button()

    def create_spinboxes(self):
        self.spinbox_day_value = tk.StringVar(value="DD")
        self.spinbox_day = ttk.Spinbox(
            self.labelframe_upper,
            values=config.SPINBOX_DAY_VALUES,
            textvariable=self.spinbox_day_value,
            width=5
        )
        self.spinbox_day.grid(row=0, column=0)

        self.spinbox_month_value = tk.StringVar(value="MM")
        self.spinbox_month = ttk.Spinbox(
            self.labelframe_upper,
            values=config.SPINBOX_MONTH_VALUES,
            textvariable=self.spinbox_month_value,
            width=5
        )
        self.spinbox_month.grid(row=0, column=1)

        self.spinbox_year_value = tk.StringVar(value="YYYY")
        self.spinbox_year = ttk.Spinbox(
            self.labelframe_upper,
            from_=1960,
            to=YEAR_TODAY,
            textvariable=self.spinbox_year_value,
            width=5
        )
        self.spinbox_year.grid(row=0, column=2)

    def create_labelframe_upper_spacer(self):
        self.labelframe_upper_spacer = tk.Canvas(
            self.labelframe_upper,
            width=config.LABELFRAME_UPPER_SPACER_WIDTH,
            height=0,
            highlightthickness=0,
            border=0
        )
        self.labelframe_upper_spacer.grid(row=0, column=3)

    def create_scrape_billboard_button(self):
        self.scrape_billboard_button = ttk.Button(
            self.labelframe_upper,
            text=config.SCRAPE_BILLBOARD_BUTTON_TEXT,
            command=self.scrape_billboard_button_clicked,
            width=config.SCRAPE_BILLBOARD_BUTTON_WIDTH
        )
        self.scrape_billboard_button.grid(row=0, column=4)

    def create_help_button_image(self):
        hbi = Image.open("help_button_icon.png")
        hbi = hbi.resize(
            config.HELP_BUTTON_IMAGE_SIZE,
            Image.BICUBIC
        )
        self.help_button_image = ImageTk.PhotoImage(hbi)

    def create_help_button(self):
        self.help_button = ttk.Button(
            self.labelframe_upper,
            image=self.help_button_image
        )
        self.help_button.grid(row=0, column=5)

    def date_entry_valid(self, year_entry, month_entry, day_entry):
        if year_entry.isnumeric() and 1960 <= int(year_entry) <= YEAR_TODAY and month_entry.isnumeric()\
                and 1 <= int(month_entry) <= 12 and day_entry.isnumeric() and 1 <= int(day_entry) <= 31:
            return True
        return False

    def scrape_billboard_button_clicked(self):
        if self.date_entry_valid(
            year_entry=self.spinbox_year_value.get(),
            month_entry=self.spinbox_month_value.get(),
            day_entry=self.spinbox_day_value.get()
        ):
            self.set_date_for_scraping("{}-{:02d}-{:02d}".format(self.spinbox_year_value.get(), int(self.spinbox_month_value.get()), int(self.spinbox_day_value.get())))
            billboard_fetcher.get_billboard_webpage(self.date_for_scraping)
            billboard_scraper.raw_html = billboard_fetcher.webpage
            billboard_scraper.make_soup()
            billboard_scraper.scrape_and_format_hot_100()
            print(billboard_scraper.hot_100_formatted)
            billboard_scraper.scrape_week_of_hot_100()
            print(billboard_scraper.week_of_hot_100_formatted)

        else:
            self.show_date_entry_not_valid_window()

    def set_date_for_scraping(self, date_string):
        self.date_for_scraping = date_string
        print(self.date_for_scraping)

    def clear_date_for_scraping(self):
        self.date_for_scraping = ""

    def show_date_entry_not_valid_window(self):
        print("Scrape button clicked")
        print("self.date_for_scraping = {}".format(self.date_for_scraping))
        self.date_entry_not_valid_window = tk.Toplevel()
        self.date_entry_not_valid_window.title(config.DATE_ENTRY_NOT_VALID_WINDOW_TITLE)
        self.date_entry_not_valid_window.resizable(False, False)
        label = ttk.Label(
            self.date_entry_not_valid_window,
            text=config.DATE_ENTRY_NOT_VALID_WINDOW_TEXT
        )
        label.grid(row=0, column=0, padx=10, pady=10)
        button = ttk.Button(
            self.date_entry_not_valid_window,
            text=config.DATE_ENTRY_NOT_VALID_WINDOW_BUTTON_TEXT,
            command=self.date_entry_not_valid_window_OK_button_clicked
        )
        button.grid(row=1, column=0, padx=10, pady=10)

    def date_entry_not_valid_window_OK_button_clicked(self):
        self.date_entry_not_valid_window.destroy()
        self.reset_spinboxes()
        self.clear_date_for_scraping()

    def reset_spinboxes(self):
        self.spinbox_day = None
        self.spinbox_month = None
        self.spinbox_year = None
        self.spinbox_day_value = None
        self.spinbox_month_value = None
        self.spinbox_year_value = None
        self.create_spinboxes()

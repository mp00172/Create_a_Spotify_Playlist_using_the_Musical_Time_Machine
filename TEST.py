

import requests
import tkinter as tk
from tkinter import ttk
from billboard_fetcher import BillboardFetcher
# from billboard_scraper import BillboardScraper
# from spotify import Spotify
from song_base import SongBase
from scrollable_frame import ScrollableFrame
from PIL import Image
from PIL import ImageTk
import datetime

YEAR_TODAY = int(str(datetime.datetime.now()).split()[0].split("-")[0])
MAIN_WINDOW_SIZE = "1400x900"
LABEL_FRAME_UP_TEXT = "Enter date:"
SCRAPE_BUTTON_TEXT = "Scrape Billboard"
LABEL_FRAME_LEFT_TEXT = "Billboard Hot100"
WEEK_LABEL_TEXT = "Week of 17.08.1985."
LABEL_FRAME_RIGHT_TEXT = "Current playlist"
SPINBOX_DAY_VALUES = [str("{:02d}").format(number) for number in range(1, 32)]
SPINBOX_MONTH_VALUES = [str("{:02d}").format(number) for number in range(1, 13)]

date_for_testing = "1985-08-12"
date_for_scraping = ""

top10_list = []


class Program:

    def __init__(self):
        self.main_window = self.create_main_window()

    def create_main_window(self):
        self.main_window = tk.Tk()


def generate_pilot_top10_list():
    for i in range(10):
        top10_list.append("Song {}".format(str(i + 1)))


generate_pilot_top10_list()


def scrape_billboard_button_clicked():
    if date_entry_valid(spinbox_year_value.get(), spinbox_month_value.get(), spinbox_day_value.get()):
        fill_date_for_scraping("{}-{:02d}-{:02d}".format(spinbox_year_value.get(), int(spinbox_month_value.get()), int(spinbox_day_value.get())))
    else:
        show_date_entry_not_valid_window()


def fill_date_for_scraping(strg):
    global date_for_scraping
    date_for_scraping = strg
    print(date_for_scraping)


def clear_date_for_scraping():
    global date_for_scraping
    date_for_scraping = ""


def date_entry_valid(year_entry, month_entry, day_entry):
    if year_entry.isnumeric() and 1960 <= int(year_entry) <= YEAR_TODAY and month_entry.isnumeric() and 1 <= int(month_entry) <= 12 and day_entry.isnumeric() and 1 <= int(day_entry) <= 31:
        return True
    return False


def show_date_entry_not_valid_window():
    window = tk.Toplevel(main_window)
    window.title("Warning")
    window.resizable(False, False)
    label = ttk.Label(window, text="Invalid day/month/year entry.")
    label.grid(row=0, column=0, pady=10, padx=10)
    button = ttk.Button(window, text="OK", command=window.destroy)
    button.grid(row=1, column=0, pady=10, padx=10)

# OVO SVE RADI!
# billboard_fetcher = BillboardFetcher()
# billboard_fetcher.get_billboard_webpage(date_for_testing)
# billboard_scraper = BillboardScraper(billboard_fetcher.webpage)
# billboard_scraper.make_soup()
# billboard_scraper.scrape_and_format_hot_100()
# print(billboard_scraper.hot_100_formatted)
# billboard_scraper.scrape_week_of_hot_100()
# print(billboard_scraper.week_of_hot_100_formatted)
# spotify = Spotify()
spotify.authenticate()
spotify.make_hot100_search(billboard_scraper.hot_100_formatted)
print(spotify.hot100_search_results)
print(type(spotify.hot100_search_results))
print(len(spotify.hot100_search_results))
songbase = SongBase()
songbase.add_hot100(spotify.hot100_search_results)
# OVO SVE RADI!

# main_window = tk.Tk()
# main_window.geometry(MAIN_WINDOW_SIZE)
# main_window.resizable(False, False)
# main_window.title(MAIN_WINDOW_SIZE)
# main_window.configure(background="black")

# UPPER FRAME

# label_frame_style = ttk.Style()

# label_frame_up = ttk.Labelframe(main_window, text=LABEL_FRAME_UP_TEXT, width=500, height=100)
# label_frame_up.grid(row=0, column=0, padx=10, pady=10, columnspan=2, sticky="N")

# spinbox_day_value = tk.StringVar(value="DD")
# spinbox_day = ttk.Spinbox(label_frame_up, values=SPINBOX_DAY_VALUES, textvariable=spinbox_day_value, width=5)
# spinbox_day.grid(row=0, column=0)
#
# spinbox_month_value = tk.StringVar(value="MM")
# spinbox_month = ttk.Spinbox(label_frame_up, values=SPINBOX_MONTH_VALUES, textvariable=spinbox_month_value, width=5)
# spinbox_month.grid(row=0, column=1)

# spinbox_year_value = tk.StringVar(value="YYYY")
# spinbox_year = ttk.Spinbox(label_frame_up, from_=1960, to=YEAR_TODAY, textvariable=spinbox_year_value, width=5)
# spinbox_year.grid(row=0, column=2)

# empty_canvas_01 = tk.Canvas(label_frame_up, width=950, height=0, highlightthickness=0, border=0)
# empty_canvas_01.grid(row=0, column=3)

# scrape_billboard_button = ttk.Button(label_frame_up, text=SCRAPE_BUTTON_TEXT, command=scrape_billboard_button_clicked,
#                                      width=12)
# scrape_billboard_button.grid(row=0, column=4)

# hbi = Image.open("help_button_icon.png")
# hbi = hbi.resize((14, 14), Image.BICUBIC)
# help_button_image = ImageTk.PhotoImage(hbi)

# help_button = ttk.Button(label_frame_up, image=help_button_image)
# help_button = ttk.Button(label_frame_up)
# help_button.grid(row=0, column=5)

# LEFT FRAME

label_frame_left = ttk.Labelframe(main_window, text=LABEL_FRAME_LEFT_TEXT)
label_frame_left.grid(row=1, column=0, sticky="NW", padx=10, pady=10, columnspan=1)

week_label = ttk.Label(label_frame_left, text=WEEK_LABEL_TEXT)
week_label.grid(row=0, column=0, columnspan=3, sticky="W", padx=10, pady=5)

scrollable_frame_left = ScrollableFrame(label_frame_left, width=640, height=300)
scrollable_frame_left.grid(row=1, column=0)

for i in range(len(billboard_scraper.hot_100_formatted)):
    artist_label = tk.Label(scrollable_frame_left.scrollable_frame, text=(billboard_scraper.hot_100_formatted[i][1]))
    artist_label.grid(row=(i + 1), column=0, sticky="w")

for i in range(len(billboard_scraper.hot_100_formatted)):
    n = tk.StringVar()
    song_of_10 = ttk.Combobox(scrollable_frame_left.scrollable_frame, textvariable=n)
    song_of_10["values"] = top10_list
    song_of_10.current(0)
    song_of_10.grid(row=(i + 1), column=1, sticky="w")

for i in range(len(billboard_scraper.hot_100_formatted)):
    button = ttk.Button(scrollable_frame_left.scrollable_frame, width=3, text="Add")
    button.grid(row=(i + 1), column=2, sticky="e")

# RIGHT FRAME

label_frame_right = ttk.LabelFrame(main_window, text=LABEL_FRAME_RIGHT_TEXT)
label_frame_right.grid(row=1, column=1, sticky="NE", padx=10, pady=10, columnspan=1)

scrollable_frame_right = ScrollableFrame(label_frame_right, width=667, height=300)
scrollable_frame_right.grid(row=0, column=0, sticky="N")

for i in range(len(billboard_scraper.hot_100_formatted)):
    artist_label = tk.Label(scrollable_frame_right.scrollable_frame,
                            text=("{} - {}".format(billboard_scraper.hot_100_formatted[i][1],
                                                   billboard_scraper.hot_100_formatted[i][2])))
    artist_label.grid(row=i, column=0, sticky="W")

for i in range(len(billboard_scraper.hot_100_formatted)):
    button1 = ttk.Button(scrollable_frame_right.scrollable_frame, width=3, text="Up")
    button1.grid(row=i, column=1, sticky="E")
    button2 = ttk.Button(scrollable_frame_right.scrollable_frame, width=3, text="Dn")
    button2.grid(row=i, column=2, sticky="E")
    button3 = ttk.Button(scrollable_frame_right.scrollable_frame, width=3, text="Rm")
    button3.grid(row=i, column=3, sticky="E")

main_window.mainloop()

import tkinter as tk
from tkinter import ttk
from PIL import Image

main = tk.Tk()
img = Image.open("help_button_icon.png")
img = img.resize((100, 100), Image.BILINEAR)

butt = ttk.Button(main, image=img)
butt.pack()
main.mainloop()
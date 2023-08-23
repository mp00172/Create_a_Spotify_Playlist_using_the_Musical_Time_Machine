import tkinter as tk
from tkinter import ttk


class ScrollableFrame(ttk.Frame):
    def __init__(self, container, width=320, height=240, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                width=width,
                height=height,
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        canvas.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, sticky="NS")


root = tk.Tk()
root.geometry("800x600")

frame = ScrollableFrame(root, width=640, height=480)


# for i in range(50):
#     ttk.Label(frame.scrollable_frame, text="Sample scrolling label").pack()

for i in range(50):
    checkbox = tk.Checkbutton(frame.scrollable_frame, text=("Checkbox no. {}".format(i + 1)))
    checkbox.grid(row=i, column=0, sticky="W")

for j in range(50):
    n = tk.StringVar()
    combo = ttk.Combobox(frame.scrollable_frame, textvariable=n, width=20)
    combo["values"] = ["Fkjhbd", "Fdkjh SJkjb", "adkfh", "Jgdpijn", "ljhbvee"]
    combo.current(0)
    combo.grid(row=j, column=1)

# canvas2 = tk.Canvas(frame.scrollable_frame)
# canvas2.grid(row=0, column=2)

for i in range(50):
    checkbox = tk.Checkbutton(frame.scrollable_frame, text=("Checkbox no. {}".format(i + 1)))
    checkbox.grid(row=i, column=3, sticky="W")

frame.grid(row=0, column=0)
root.mainloop()

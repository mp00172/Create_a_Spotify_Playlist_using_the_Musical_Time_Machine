import tkinter as tk
from tkinter import ttk

class ScrollableFrame(ttk.Frame):
    def __init__(self, container, *args, **kwargs):
        super().__init__(container, *args, **kwargs)
        canvas = tk.Canvas(self)
        scrollbar = ttk.Scrollbar(self, orient="vertical", command=canvas.yview)
        self.scrollable_frame = ttk.Frame(canvas)
        self.scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(
                scrollregion=canvas.bbox("all")
            )
        )
        canvas.create_window((0, 0), window=self.scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)
        # canvas.pack(side="left", fill="both", expand=True)
        # scrollbar.pack(side="right", fill="y")
        canvas.grid(row=0, column=0)
        scrollbar.grid(row=0, column=1, sticky="NSE")

main = tk.Tk()
label_frame = ttk.LabelFrame(main, text="Nekakav tekst za label frame")
label_frame.grid(row=0, column=0, padx=10, pady=10)

canvas1 = tk.Canvas(label_frame, width=200, height=100)
canvas1.grid(row=0, column=0, columnspan=2)

label = ttk.Label(canvas1, text="Week of 18/08/1934")
label.grid(row=0, column=0)

# canvas2 = ScrollableFrame(label_frame, width=800, height=500)
canvas2 = tk.Canvas(label_frame, width=400, height=500)
canvas2.grid(row=1, column=0, columnspan=1)
canvas2.grid_propagate(0)

for i in range(50):
    checkbox = tk.Checkbutton(canvas2, text=("Checkbox no. {}".format(i + 1)))
    checkbox.grid(row=i, column=0)

for j in range(50):
    n = tk.StringVar()
    combo = ttk.Combobox(canvas2, textvariable=n)
    combo["values"] = ["Fkjhbd", "Fdkjh SJkjb", "adkfh", "Jgdpijn", "ljhbvee"]
    combo.current(0)
    combo.grid(row=j, column=1)

scrollbar = ttk.Scrollbar(canvas2, orient="vertical", command=canvas2.yview) #
scrollable_frame = ttk.Frame(canvas2) #
scrollable_frame.bind(
    "<Configure>",
    lambda e: canvas2.configure(scrollregion=canvas2.bbox("all")
    )
)
canvas2.create_window((0, 0), window=scrollable_frame, anchor="nw") #
canvas2.configure(yscrollcommand=scrollbar.set) #
canvas2.grid(row=0, column=0)
scrollbar.grid(column=2, row=0,  sticky="NS") #

canvas4 = tk.Canvas(label_frame, width=200, height=100)
canvas4.grid(row=2, column=0)

for k in range(3):
    button = tk.Button(canvas4, text="Button no. {}".format(k + 1))
    button.grid(row=0, column=k)

main.mainloop()
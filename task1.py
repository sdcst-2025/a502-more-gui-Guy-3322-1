import tkinter as tk 
from tkinter import *
from tkinter import ttk


window=tk.Tk()
window.title("tk")
window.geometry("390x100")

text1 =tk.Label(window, text = "Principal")
text1.grid(row = 1 , column = 1)
entry1 = tk.Entry(window)
entry1.grid(row = 2, column = 1)

text2 =tk.Label(window, text = "Interest Rate")
text2.grid(row = 1 , column = 2)
entry2 = tk.Entry(window)
entry2.grid(row = 2, column = 2)

text3 =tk.Label(window, text = "Amount")
text3.grid(row = 4 , column = 1)
entry3 = tk.Entry(window)
entry3.grid(row = 4, column = 2)

text4 =tk.Label(window, text = "-")
text4.grid(row = 3 , column = 1)

label = ttk.Label(window, text="Choose a Year:")
label.grid(row = 1, column = 3)
start_year = 1950

years = [str(y) for y in range(2026, start_year - 1, -1)]

year_var = tk.StringVar()


year_combobox = ttk.Combobox(
    window,
    textvariable=year_var,
    values=years,
    state="readonly", 
)
year_combobox.grid(row = 2, column = 3)

window.mainloop()
import tkinter as tk 
from tkinter import *



window=tk.Tk()
window.title("POKEMON ADVENTURE")
window.geometry("700x600")



maingame = PhotoImage(file="main.png")
photo = tk.Label(window, image=maingame)

mini = PhotoImage(file="minimap.png")
map = tk.Label(window, image=mini)

logo = PhotoImage(file="logo.png")
logon = tk.Label(window, image=logo)

textmini = tk.Label(window, text = " MINI MAP")


north = tk.Button(window,text="N", width=2, height=1)
nw = tk.Button(window,text="NW", width=2, height=1)
west = tk.Button(window,text="W", width=2, height=1)
sw = tk.Button(window,text="SW", width=2, height=1)
south = tk.Button(window,text="S", width=2, height=1)
se = tk.Button(window,text="SE", width=2, height=1)
east = tk.Button(window,text="E", width=2, height=1)
ne = tk.Button(window,text="NE", width=2, height=1)



mapb = tk.Button(window,text="MAP", width=13, height=2)
inv = tk.Button(window,text="INVENTORY", width=13, height=2)
dex = tk.Button(window,text="POKEDEX", width=13, height=2)
team = tk.Button(window,text="ROSTER", width=13, height=2)
notes = tk.Button(window,text="JOURNAL", width=13, height=2)
help = tk.Button(window,text="HELP", width=13, height=2)
shop = tk.Button(window,text="SHOP", width=13, height=2)



photo.place(x=10,y=0)
map.place(x=550,y=50)
logon.place(x=280,y=470)
textmini.place(x=568,y=25)


north.place(x=35, y=450)
nw.place(x=10, y=450)
west.place(x=10, y=475)
sw.place(x=10, y=500)
south.place(x=35, y=500)
se.place(x=59, y=500)
east.place(x=59, y=475)
ne.place(x=59, y=450)


mapb.place(x=550, y=150)
inv.place(x=550, y=190)
dex.place(x=550, y=230)
team.place(x=550, y=270)
help.place(x=550, y=310)
shop.place(x=550, y=350)



window.mainloop()
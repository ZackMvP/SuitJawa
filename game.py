import random
import tkinter as tk
import time

def choice():
    selection = random.randint(1, 3)
    return selection

def compare(you, ai):
    if you == 1:
        if ai == 1:
            return "Seri, AI memilih gajah"
        elif ai == 2:
            return "Menang, AI memilih orang"
        elif ai == 3:
            return "Kalah, AI memilih semut"
    elif you == 2:
        if ai == 1:
            return "Kalah, AI memilih gajah"
        elif ai == 2:
            return "Seri, AI memilih orang"
        elif ai == 3:
            return "Menang, AI memilih semut"
    elif you == 3:
        if ai == 1:
            return "Menang, AI memilih gajah"
        elif ai == 2:
            return "Kalah, AI memilih orang"
        elif ai == 3:
            return "Seri, AI memilih semut"

def battle(you):
    WinTab = tk.Toplevel(gui)
    WinTab.geometry("648x461")
    WinTab.config(bg='#C9ADA7')
    ai = choice()
    winner = compare(you, ai)

    title = tk.Label(
        WinTab,
        text='Permainan Suit Jawa',
        bg='#F2E9E4',
        font=('Inknut Antiqua', 34)
    )
    title.pack()
    win = tk.Label(WinTab, text=winner, font=('Inknut Antiqua', 18))
    win.pack()

gui = tk.Tk()
gui.geometry("648x461")
gui.config(bg='#C9ADA7')

exitButton = tk.Button(
    text='X',
    font=('Arial', 12),
    bg='red',
    activebackground='red',
    command=exit
)
exitButton.pack(padx=(601, 0), pady=(8, 0))

title = tk.Label(
    text='Permainan Suit Jawa',
    bg='#F2E9E4',
    font=('Inknut Antiqua', 40)
)
title.pack(pady=(0, 0))

button_frame = tk.Frame(gui, bg='#C9ADA7')
button_frame.pack()

gajah = tk.Button(
    button_frame,
    text='Gajah',
    font=('Inknut Antiqua', 18),
    bg='#9A8C98',
    height=-5,
    command=lambda: battle(1)
)
gajah.pack(side='left')

orang = tk.Button(
    button_frame,
    text='Orang',
    font=('Inknut Antiqua', 18),
    bg='#9A8C98',
    height=-5,
    command=lambda: battle(2)
)
orang.pack(side='left')

semut = tk.Button(
    button_frame,
    text='Semut',
    font=('Inknut Antiqua', 18),
    bg='#9A8C98',
    height=-5,
    command=lambda: battle(3)
)
semut.pack(side='left')

gui.mainloop()
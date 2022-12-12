from tkinter import *
import pullInfo, pullInfoLibro
import tkinter as tk

from tkinter import *
from tkmacosx import *
from tkinter.ttk import Sizegrip
import time

master = tk.Tk()
master.title("TreasureChest")
label = tk.Label(text="Welcome to Standalone Inventory",
                 foreground="white",
                 background="black",
                 width=10,
                 height=10
                 )


def x():
    exec(open('/Users/jose.pacheco/PycharmProjects/TreasureChestDemo/pullInfoLibro.py').read())


def y():
    exec(open('/Users/jose.pacheco/PycharmProjects/TreasureChestDemo/pullInfo.py').read())


firstButton = tk.Button(master, text="Zapas", command=x)
firstButton.pack()

secondButton = tk.Button(master, text="Libros", command=y)
secondButton.pack()

mainloop()

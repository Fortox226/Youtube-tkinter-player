import tkinter as tk
from main import *

def startWindow():    
    root = tk.Tk()
    root.geometry('400x400')

    label = tk.Label(root, text='Wklej link do filmu: ')
    label.pack()

    entry = tk.Entry(root)
    entry.pack()

    button = tk.Button(root, text='Rozpocznij pobieranie', command=lambda: allFromMain( entry.get()))
    button.pack()

    root.mainloop()
startWindow()
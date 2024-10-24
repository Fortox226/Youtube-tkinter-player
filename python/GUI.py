
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage
from main import *

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Documents\GitHub\Youtube-tkinter-player\python\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("500x300")
window.configure(bg = "#FF4444")


canvas = Canvas(
    window,
    bg = "#FF4444",
    height = 300,
    width = 500,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    86.0,
    18.0,
    anchor="nw",
    text="YouTube Downloader",
    fill="#FFFFFF",
    font=("AROneSans Regular", 32 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    347.5,
    98.5,
    image=entry_image_1
)
entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=323.5,
    y=80.0,
    width=48.0,
    height=35.0
)

canvas.create_text(
    315.0,
    61.0,
    anchor="nw",
    text="Format",
    fill="#FFFFFF",
    font=("AROneSans Regular", 14 * -1)
)

canvas.create_text(
    105.0,
    61.0,
    anchor="nw",
    text="Paste link",
    fill="#FFFFFF",
    font=("AROneSans Regular", 14 * -1)
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    199.5,
    98.5,
    image=entry_image_2
)
entry_2 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_2.place(
    x=113.5,
    y=80.0,
    width=172.0,
    height=35.0
)

image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    245.0,
    152.0,
    image=image_image_1
)

button_image_1 = PhotoImage(
    file=relative_to_assets("button_1.png"))
button_1 = Button(
    image=button_image_1,
    borderwidth=0,
    highlightthickness=0,
    command=lambda: allFromMain(entry_2.get(), entry_1.get()),
    relief="flat"
)
button_1.place(
    x=135.0,
    y=134.0,
    width=220.0,
    height=36.0
)
window.resizable(False, False)
window.mainloop()

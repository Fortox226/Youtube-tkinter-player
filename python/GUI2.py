from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox
from pathlib import Path
from searcher import youtube_search
from main import *
import html
from tkinter import *
from main import *
from downlad_information import *
import os

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"./assets/frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

#Główny plik

root = Tk()
root.title("Yt-Searcher")
root.geometry("600x400")
root.configure(bg = "#FF4444")


canvas = Canvas(
    root,
    bg = "gray",
    height = 400,
    width = 600,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

frame = Frame(root, width=400, height=200, bg='gray')
frame.place(x=90, y=120.5)  # Ustawienie ramki w lewym górnym rogu okna



def showResult(query):
    results = youtube_search(query)

    for widget in frame.winfo_children():
        widget.destroy()

    for index, item in enumerate(results):
        video_id = item['id'].get('videoId')
        if video_id:
            coded_title = item['snippet']['title']
            title = html.unescape(coded_title)
            print(title)

            def on_button_click(v_id):
                create_download_ui(root, f'https://www.youtube.com/watch?v={v_id}')
                

            button = Button(frame, text=title, width=50)
            button.config(command=lambda v=video_id: on_button_click(v))
            button.pack(pady=5)

def open_folder():
    folder_path = "./Videos"
    absolute_path = os.path.abspath(folder_path)

    if os.path.exists(absolute_path):
        if os.name == 'nt':  # Windows
            os.startfile(absolute_path)
        elif os.name == 'posix':  # macOS/Linux
            os.system(f'xdg-open "{absolute_path}"')
    else:
        messagebox.showerror("Błąd", f"Folder '{folder_path}' nie istnieje!")


button3 = Button(
    text="Open Videos Folder",
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    command=lambda: open_folder(),
)

button3.place(
    x=10.0,
    y=335.0,
    width=120,
    height=50
)

canvas.place(x = 0, y = 0)
canvas.create_text(
    170.0,
    18.0,
    anchor="nw",
    text="YouTube Searcher",
    fill="#FFFFFF",
    font=("AROneSans Regular", 32 * -1)
)

entry_1 = Entry(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=80.5,
    y=80.0,
    width=300.0,
    height=35.0
)

button_image_1 = PhotoImage(
    file=relative_to_assets("Frame1.png"))

button1 = Button(
    image=button_image_1,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    command=lambda: showResult(entry_1.get())
)

button1.place(
    x=400.5,
    y=80.0,
    width=100.0,
    height=35.0
)

root.mainloop()
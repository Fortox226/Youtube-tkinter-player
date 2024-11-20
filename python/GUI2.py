from tkinter import Tk, Canvas, Entry, Text, Button, PhotoImage, Frame, messagebox
from pathlib import Path
# from searcher import youtube_search
from main import *
import html





OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path(r"C:\Users\Admin\Documents\GitHub\Youtube-tkinter-player\python\assets\frame0")


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)

def openDownloader():
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
        file=relative_to_assets("entry_1.png"),
        master=window
    )
    entry_bg_1= canvas.create_image(
        347.5,
        98.5,
        image=entry_image_1
    )
    # entry_1 = Entry(
    #     master=window,
    #     bd=0,
    #     bg="#D9D9D9",
    #     fg="#000716",
    #     highlightthickness=0
    # )
    # entry_1.place(
    #     x=323.5,
    #     y=80.0,
    #     width=48.0,
    #     height=35.0
    # )

    # canvas.create_text(
    #     315.0,
    #     61.0,
    #     anchor="nw",
    #     text="Format",
    #     fill="#FFFFFF",
    #     font=("AROneSans Regular", 14 * -1)
    # )

    canvas.create_text(
        105.0,
        61.0,
        anchor="nw",
        text="Paste link",
        fill="#FFFFFF",
        font=("AROneSans Regular", 14 * -1)
    )

    entry_image_2 = PhotoImage(
        file=relative_to_assets("entry_2.png"), master=window)
    entry_bg_2 = canvas.create_image(
        199.5,
        98.5,
        image=entry_image_2
    )
    entry_2 = Entry(
        master=window,
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
        file=relative_to_assets("image_1.png"), master=window)
    image_1 = canvas.create_image(
        245.0,
        152.0,
        image=image_image_1
    )

    button_image_1 = PhotoImage(
        file=relative_to_assets("button_1.png"), master=window)
    button_1 = Button(
        master=window,
        image=button_image_1,
        borderwidth=0,
        highlightthickness=0,
        command=lambda: allFromMain(entry_2.get()),
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

#Główny plik

root = Tk()

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

            def on_button_click(btn, v_id):
                root.clipboard_clear()
                root.clipboard_append(f'https://www.youtube.com/watch?v={v_id}')
                messagebox.showinfo("Skopiowano", f"link https://www.youtube.com/watch?v='{v_id}' został skopiowany do schowka!")

            button = Button(frame, text=title, width=50)
            button.config(command=lambda b=button, v=video_id: on_button_click(b, v))
            button.pack(pady=5)

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

button_image_2 = PhotoImage(
    file=relative_to_assets("Frame2.png"))

button2 = Button(
    image=button_image_2,
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0,
    command=lambda: openDownloader()
)

button2.place(
    x=80.0,
    y=320.0,
    width=100.0,
    height=35.0
)

root.mainloop()
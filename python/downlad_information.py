import threading
from tkinter import Toplevel, Label
from tkinter import ttk
from main import allFromMain
from PIL import Image, ImageTk

def create_download_ui(root, link):
    """
    Tworzy okno z paskiem postępu i uruchamia pobieranie w oddzielnym wątku.

    Args:
        root: Główne okno aplikacji (Tkinter).
        link: Link do wideo z YouTube do pobrania.
    """
    # Tworzymy nowe okno dla pobierania
    download_window = Toplevel(root)
    download_window.title("Downloading")

    # Etykieta stanu
    progress_label = Label(download_window, text="Initializing...")
    progress_label.pack(pady=10)

    # Pasek postępu
    progress_bar = ttk.Progressbar(download_window, orient="horizontal", length=300, mode="determinate")

    # Konfiguracja paska postępu
    progress_bar['value'] = 0
    progress_bar['maximum'] = 100

    # Uruchamiamy pobieranie w oddzielnym wątku
    threading.Thread(target=allFromMain, args=(link, progress_bar, progress_label)).start()
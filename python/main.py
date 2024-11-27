from yt_dlp import YoutubeDL
import requests
import time

def allFromMain(link, progress_bar, progress_label):
    """
    Pobiera wideo z YouTube za pomocą yt_dlp i aktualizuje pasek postępu.

    Args:
        link: Link do wideo na YouTube.
        progress_bar: Obiekt paska postępu (ttk.Progressbar).
        progress_label: Label do wyświetlania statusu.
    """
    def progress_hook(d):
        if d['status'] == 'downloading':
            downloaded = d.get('_percent_str', '').strip('%')
            speed = d.get('_speed_str', 'N/A')
            eta = d.get('eta', 'N/A')
            
            # Aktualizuj pasek postępu
            try:
                progress_bar['value'] = float(downloaded)
                progress_label.config(text=f"Downloading... {downloaded}% | Speed: {speed} | ETA: {eta}s")
            except ValueError:
                pass
        elif d['status'] == 'finished':
            progress_label.config(text="Download complete!")

    def main():
        ydl_opts = {
            'format': 'best',
            'outtmpl': './Videos/%(title)s.%(ext)s',
            'noplaylist': True,
            'progress_hooks': [progress_hook],  # Dodajemy hook do śledzenia postępu
        }
        with YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])


    # Uruchamiamy pobieranie

    def is_connected():
        try:
            # Wykonaj zapytanie do znanego adresu URL
            requests.get("https://www.google.com", timeout=5)
            return True
        except requests.ConnectionError:
            return False
    is_connected()

    while True:
        if not is_connected():
            print("Brak połączenia z internetem. Sprawdzanie ponownie...")
            time.sleep(5)  # Czekaj 5 sekund przed kolejnym sprawdzeniem
        else:
            print("Połączenie z internetem zostało nawiązane!")
            main()
            break
# allFromMain('https://www.youtube.com/watch?v=wqeGPX7TRv0')
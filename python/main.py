import yt_dlp
import requests
import time

def allFromMain(link):
    def main():
        ydl_opts = {
            'format': 'best',
            'outtmpl': '%(title)s.%(ext)s',
            'noplaylist': True,
        }
                
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])
        

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
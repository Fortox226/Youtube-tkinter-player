import yt_dlp
import requests
import time

ydl_opts = {}

def allFromMain():
    def main():
        def dwl_vid(video_url):
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                ydl.download([video_url])

        channel = 1
        while channel == 1:
            link_of_the_video = input("Copy & paste the URL of the YouTube video you want to download: ")
            zxt = link_of_the_video.strip()

            dwl_vid(zxt)
            channel = int(input("Enter 1 if you want to download more videos\nEnter 0 if you are done: "))

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
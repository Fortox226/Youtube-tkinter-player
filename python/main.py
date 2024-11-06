import yt_dlp
import requests
import time
import subprocess

ffmpeg_path = "C:/ffmpeg"

def allFromMain(link, format):
    def main():
        with yt_dlp.YoutubeDL() as ydl:
            if format == 'mp4':
                ydl_opts = {
                     'format': 'best',
                     'outtmpl': '%(title)s.%(ext)s',
                     'noplaylist': True,
                 }
                
            elif format == 'mp3':
                ydl_opts = {
                    'format': 'bestaudio/best',
                    'outtmpl': '%(title)s.%(ext)s',
                    'noplaylist': True,
                }

            else:
                print("Nieprawidłowy wybór formatu.")
                return
            
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([link])

            if format == 'mp3':
                filename = ydl.prepare_filename(ydl.extract_info(link, download=False))
                file_extension = filename.split('.')[-1]
                
                if file_extension != 'mp3':  # Jeśli to nie jest mp3, konwertuj
                    mp3_filename = filename.replace(file_extension, 'mp3')
                    command = [
                        ffmpeg_path, '-i', filename, '-vn', '-ar', '44100', '-ac', '2', '-b:a', '192k', mp3_filename
                    ]
                    subprocess.run(command)  # Uruchamiamy FFmpeg do konwersji

                    print(f"Plik audio zapisany jako {mp3_filename}")

        

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
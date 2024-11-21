from bs4 import BeautifulSoup
import requests

strona = requests.get("https://www.youtube.com/watch?v=IbTGWRkkihI")

soup = BeautifulSoup(strona.content, 'html.parser')

print(soup.find("yt-formatted-string"))

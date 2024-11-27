from googleapiclient.discovery import build
from API import *

# Ustaw swój klucz API
API_KEY = API

def youtube_search(query, max_results=5):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    )
    response = request.execute()

    return response['items']

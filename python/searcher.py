import os
from googleapiclient.discovery import build

# Ustaw swój klucz API
API_KEY = 'AIzaSyA8QVQKMP3iCUWcIX5wha6bCPMuA8FS6Rs'

def youtube_search(query, max_results=6):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    )
    response = request.execute()

    return response['items']
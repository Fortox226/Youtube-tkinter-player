import os
from googleapiclient.discovery import build

# Ustaw swój klucz API
API_KEY = 'AIzaSyA8QVQKMP3iCUWcIX5wha6bCPMuA8FS6Rs'

def youtube_search(query, max_results=4):
    youtube = build('youtube', 'v3', developerKey=API_KEY)

    request = youtube.search().list(
        q=query,
        part='id,snippet',
        maxResults=max_results
    )
    response = request.execute()

    return response['items']

def main(query):
    # query = input("Wpisz zapytanie do wyszukania: ")
    results = youtube_search(query)

#     for item in results:
#         video_id = item['id'].get('videoId')
#         if video_id:
#             title = item['snippet']['title']
#             print(f'Tytuł: {title}, URL: https://www.youtube.com/watch?v={video_id}')

# if __name__ == '__main__':
#     main()
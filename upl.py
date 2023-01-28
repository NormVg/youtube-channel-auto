from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
import os
import google
import google_auth_oauthlib
import ast


DEVELOPER_KEY = "AIzaSyDaZXxMgzuYQzRg5o9xvhQbiiLv-tuHSNc"

scopes = ["https://www.googleapis.com/auth/youtube.upload"]
client_secrets_file = "cred.json"
os.environ["OAUTHLIB_INSECURE_TRANSPORT"] = "1"



flow = google_auth_oauthlib.flow. InstalledAppFlow.from_client_secrets_file(client_secrets_file, scopes)
credentials = flow.run_console()
youtube = build('youtube', 'v3', credentials=credentials)
def upload():
    try:

        file_metadata = {'name': 'video.mp4'}
        media = MediaFileUpload('video.mp4', mimetype='video/mp4')


        request = youtube.videos().insert(
            part='snippet, status',
            body={
                'snippet': {
                    'title': 'My video #shorts',
                    'description': '#shorts',
                    'tags': ['reddit', 'interesting', 'story',"shorts"],
                    'categoryId': '22'
                },
                'status': {
                    'privacyStatus': 'public'
                }
            },
            media_body=media
        )

        # execute the request
        response = request.execute()

        # print the response
        print(response)

    except HttpError as error:
        print(f'An error occurred: {error}')

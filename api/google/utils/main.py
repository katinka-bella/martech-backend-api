import requests
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow

SCOPES = [
        "https://www.googleapis.com/auth/analytics", 
        "https://www.googleapis.com/auth/analytics.edit"
]

REDIRECT_URL = "https://localhost:8080/callback"

class UtilsGoogle:
    def create_access_token(
        CLIENT_ID, CLIENT_SECRET, SCOPES, PATH_SECRETS_FILE, REDIRECT_URL
    ):

        # Create the flow object
        flow = InstalledAppFlow.from_client_secrets_file(
            PATH_SECRETS_FILE,
            scopes=SCOPES,
            redirect_uri=REDIRECT_URL
        )

        # Get authorization URL
        auth_url, _ = flow.authorization_url(access_type='offline')

        # Open authorization URL in a web browser and authorize the application
        print("Please go to this URL: {}".format(auth_url))
        authorization_response = input("Enter the full callback URL: ")

        # Get the authorization code from the response
        flow.fetch_token(authorization_response=authorization_response)

        # Create credentials object from the flow object
        creds = flow.credentials

        return creds.token
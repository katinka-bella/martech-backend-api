from dataclasses import dataclass
import requests
from google_auth_oauthlib.flow import InstalledAppFlow

# TODO: SCOPE

@dataclass
class GoogleBase:
    client_id: str
    client_secret: str
    secret_file_path: str
    REDIRECT_URL = "https://localhost:8080/callback"

    def create_access_token(self, scopes):
        # Create the flow object
        flow = InstalledAppFlow.from_client_secrets_file(
            self.secret_file_path, scopes=scopes, redirect_uri=self.REDIRECT_URL
        )

        # Get authorization URL
        auth_url, _ = flow.authorization_url(access_type="offline")

        # Open authorization URL in a web browser and authorize the application
        print("Please go to this URL: {}".format(auth_url))
        authorization_response = input("Enter the full callback URL: ")

        # Get the authorization code from the response
        flow.fetch_token(authorization_response=authorization_response)

        # Create credentials object from the flow object
        creds = flow.credentials
        self.access_token = creds.token

        return self.access_token
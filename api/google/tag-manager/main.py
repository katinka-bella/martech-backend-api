from dataclasses import dataclass
import requests
from google_auth_oauthlib.flow import InstalledAppFlow


@dataclass
class GoogleBase:
    client_id: str
    client_secret: str
    secret_file_path: str
    SCOPES = [
        "https://www.googleapis.com/auth/tagmanager.edit.containers",
        "https://www.googleapis.com/auth/tagmanager.readonly",
    ]
    REDIRECT_URL = "https://localhost:8080/callback"

    def create_access_token(self):
        # Create the flow object
        flow = InstalledAppFlow.from_client_secrets_file(
            self.secret_file_path, scopes=self.SCOPES, redirect_uri=self.REDIRECT_URL
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


@dataclass
class GoogleAnalyticsOperator(GoogleBase):
    api_key: str
    api_action_list = [
        "triggers"
    ]

    base_url = "https://tagmanager.googleapis.com/tagmanager/v2/accounts"

    def set_api_action(self):
        print("SELECT NUMBER")
        for num, item in enumerate(self.api_action_list):
            print(num, ": ", item)

        try:
            input_number = int(input())
            self.api_action = self.api_action_list[input_number]
            print(f"✅ You chose {self.api_action} method ✅")

        except:
            print("❌Check the input value. Only number❌")
            exit()

    def get_full_api_url(self, account_id, container_id, workspace_id):
        full_api_url = (
            f"{self.base_url}/{account_id}/containers/{container_id}/workspaces/{workspace_id}/{self.api_action}?key={self.api_key}"
        )
        return full_api_url

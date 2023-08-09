from dataclasses import dataclass
from google.cloud import storage
from google.oauth2.service_account import Credentials


@dataclass
class GoogleCloudeStorage:
    path_server_account_key: str
    bucket_api = "martech-api-bucket"
    bucket_config = "martech-config-bucket"

    def read_bucket(self, bucket_name, file_path):
        creds = Credentials.from_service_account_file(self.path_server_account_key)
        self.client = storage.Client(credentials=creds)
        get_gcs_bucket = self.client.get_bucket(bucket_name)
        gcs_blob = get_gcs_bucket.blob(file_path)
        self.contents_gcs = gcs_blob.download_as_string()
        return self.contents_gcs
    
    def read_backend_api_method(self):
        API_METHODS_FILE_PATH = "api/google/analytics/main.py"
        contents_token = self.read_bucket(self.bucket_api, API_METHODS_FILE_PATH)
        return contents_token

    def read_api_request(self):
        API_METHODS_FILE_PATH = "utils/request.py"
        contents_token = self.read_bucket(self.bucket_api, API_METHODS_FILE_PATH)
        return contents_token

    def read_backend_api_utils(self):
        UTILS_FILE_PATH = "api/google/analytics/utils.py"
        contents_utils = self.read_bucket(self.bucket_api, UTILS_FILE_PATH)
        return contents_utils

    def read_backend_api_settings(self):
        SETTINGS_FILE_PATH = "gcp/settings.py"
        contents_settings = self.read_bucket(self.bucket_config, SETTINGS_FILE_PATH)
        return contents_settings

    def read_client_config(self, path_client_config_data):
        client_inputs = self.read_bucket(self.bucket_config, path_client_config_data)
        return client_inputs
        

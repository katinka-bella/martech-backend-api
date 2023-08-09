from google.cloud import storage
import glob

SERVER_ACCOUNT_KEY_PATH = 'config/service_account_cred.json'
client = storage.Client.from_service_account_json(json_credentials_path=SERVER_ACCOUNT_KEY_PATH)
bucket = storage.Bucket(client, 'martech-api-bucket-test')

for str_path_file in glob.glob('api/**'):
    print(f'Uploading {str_path_file}')
    # The name of file on GCS once uploaded
    blob = bucket.blob(str_path_file)
    # The content that will be uploaded
    blob.upload_from_filename(str_path_file)
    print(f'Path in GCS: {str_path_file}')
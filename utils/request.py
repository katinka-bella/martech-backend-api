import requests 
    
def read_api_obj(full_api_url, access_token):
    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json"
    }

    response = requests.get(full_api_url, headers=headers, timeout=100)
    print("✅ API Read template ✅")
    print(response.content)
    return response.content
        

def create_api_obj(full_api_url, access_token, data):

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Accept": "application/json",
        "Content-Type": "application/json",
    }

    for item in data:
        response = requests.post(full_api_url, headers=headers, json=item, timeout=100)
        
        print(response.content)
    print("🔥 API Runn Successful 🔥")

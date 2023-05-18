import requests

class google_analytics_operator:
    def create_custom_metric():
        print("custom metric was created!")
    
    def generate_ga4_custom_dimensions(
        property_ids: list,
        custom_dimensions: list,
        access_token: str,
        api_key: str
    ):

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        for property_id in property_ids:
            url = f'https://analyticsadmin.googleapis.com/v1alpha/properties/{property_id}/customDimensions?key={api_key}'
            print(property_id)
            for item in custom_dimensions:
                data = {
                    'description': item.get("description"),
                    'displayName': item.get("displayName"),
                    'scope': item.get("scope"),
                    'parameterName': item.get("parameterName")
                }

                response = requests.post(url, headers=headers, json=data)
                print(response.content)

    def get_custom_dimension(df):
        # Create a new list of dictionaries with the desired keys
        custom_dimention = []
        for index, row in df.iterrows():
            custom_dimention.append({
                "displayName": row["displayName"] if not pd.isna(row["displayName"]) else "",
                "parameterName": row["parameterName"] if not pd.isna(row["parameterName"]) else "",
                "scope": row["scope"] if not pd.isna(row["scope"]) else "",
                "description": row["description"] if not pd.isna(row["description"]) else ""
            })
        return custom_dimention

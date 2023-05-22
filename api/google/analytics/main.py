import requests

class google_analytics_operator:
    def create_custom_metrics(inputs):
        print(f"{'#'*30}")
        print(f"CUSTOM METRICS WERE CREATED !")
        print(f"{'#'*30}")

    def read_custom_metrics():
        print("custom metric was read!")

    def update_custom_metrics():
        print("custom metric was updated!")

    def delete_custom_metrics():
        print("custom metric was deleted!")

    def create_custom_dimensions(
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

    def read_custom_dimensions(df):
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
    

    def create_google_ads_link(
        property_ids: list,
        customer_ids: list,
        access_token: str,
        api_key: str
    ):

        headers = {
            'Authorization': f'Bearer {access_token}',
            'Accept': 'application/json',
            'Content-Type': 'application/json'
        }

        for property_id in property_ids:
            url = f'https://analyticsadmin.googleapis.com/v1alpha/properties/{property_id}/googleAdsLinks?key={api_key}'
            print(property_id)
         
            for customer_id in customer_ids:
                data = {
                    'adsPersonalizationEnabled': 'true',
                    'customerId': customer_id
                }

                response = requests.post(url, headers=headers, json=data)
                print(response.content)

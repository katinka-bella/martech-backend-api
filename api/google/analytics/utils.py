import pandas as pd
from io import BytesIO
import json
def convert_bool_to_str(d):
    for key, value in d.items():
        if isinstance(value, dict):
            convert_bool_to_str(value)
        elif isinstance(value, bool):
            d[key] = str(value).lower()


def create_api_input_data(input_data, api_output, api_action):
    api_target_item_list = []

    match api_action:
        case "customDimensions":
            df = pd.read_excel(
                BytesIO(input_data), sheet_name="CustomDimension"
            )

            for index, row in df.iterrows():
                data = {
                    'displayName': row["displayName"] if not pd.isna(row["displayName"]) else "",
                    'parameterName': row["parameterName"] if not pd.isna(row["parameterName"]) else "",
                    'scope': row["scope"] if not pd.isna(row["scope"]) else "",
                    'description': row["description"] if not pd.isna(row["description"]) else ""
                }
                api_target_item_list.append(data)

        case "googleAdsLinks":
            df = pd.read_excel(
                BytesIO(input_data), sheet_name="GoogleAdsCustomer"
            )
            for customer_id in df["customer_id"].tolist():
                data = {
                    "adsPersonalizationEnabled": "false",
                    "customerId": str(customer_id),
                }
                api_target_item_list.append(data)
        
        case "audiences":
            # Convert bytes to a string
            output_str = api_output.decode("utf-8")

            # Find the starting index of the JSON object
            start_index = output_str.find('{')

            # Extract the JSON substring
            json_str = output_str[start_index:]

            # Convert the JSON string to a Python dictionary
            data_dict = json.loads(json_str)

            # Function to convert boolean values to string format

            audiences_list = data_dict['audiences']
            for audience in audiences_list:
                audience_dict = {}
                for key, value in audience.items():
                    if key != 'name':
                        if isinstance(value, str):
                            value = value.strip()  # Remove leading/trailing whitespaces
                        audience_dict[key] = value

                # Convert boolean values to string format
                convert_bool_to_str(audience_dict)
           
                api_target_item_list.append(audience_dict)    
            
        case _:
            print("❌Check the dataframe❌")
            exit()

    print("✅ Input data was read ✅")
    return api_target_item_list


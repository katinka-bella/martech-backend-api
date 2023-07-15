from dataclasses import dataclass
import requests
from google_auth_oauthlib.flow import InstalledAppFlow

from uitls.google_api import GoogleBase


@dataclass
class GoogleAnalyticsOperator(GoogleBase):
    property_ids: list
    api_key: str
    api_action_list = ["customDimensions", "customMetrics", "googleAdsLinks"]
    base_url = "https://analyticsadmin.googleapis.com/v1alpha/properties"

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
        
        return self.api_action

    def run_api(self, target_item_list):
        headers = {
            "Authorization": f"Bearer {self.access_token}",
            "Accept": "application/json",
            "Content-Type": "application/json",
        }

        print(f"✅ {self.api_action} API Running ✅")

        item_count = 0
        for property_id in self.property_ids:
            self.api_url = (
                f"{self.base_url}/{property_id}/{self.api_action}?key={self.api_key}"
            )
            print("PROPERTY: ", property_id)

            for target_item in target_item_list:
                response = requests.post(
                    self.api_url, headers=headers, json=target_item
                )
                print(response.content)

                if response.status_code == 200:
                    item_count += 1

        print("🔥 API Runn Successful 🔥")
        print(
            f"🔥 For {len(self.property_ids)} GA4 properties were created {item_count} items 🔥"
        )
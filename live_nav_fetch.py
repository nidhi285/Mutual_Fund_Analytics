import requests
import pandas as pd
import os

SCHEME_CODE = "125497"  # HDFC Top 100 Direct

url = f"https://api.mfapi.in/mf/{SCHEME_CODE}"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()

    nav_data = pd.DataFrame(data["data"])

    os.makedirs("Data/Raw", exist_ok=True)

    output_file = "Data/Raw/nav_history.csv"
    nav_data.to_csv(output_file, index=False)

    print(f"NAV data saved to {output_file}")
    print(nav_data.head())
else:
    print("Failed to fetch NAV data")
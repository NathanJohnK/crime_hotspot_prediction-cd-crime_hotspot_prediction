import requests
import pandas as pd

def fetch_crime_data(lat, lng, date):
    url = f"https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={date}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
    else:
        print("Error fetching data:", response.status_code)
        return None

if __name__ == "__main__":
    crimes = fetch_crime_data(52.629729, -1.131592, "2024-01")
    df = pd.DataFrame(crimes)
    df.to_csv("crime_data.csv", index=False)
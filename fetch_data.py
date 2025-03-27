import requests
import pandas as pd

## API request
#Convert Data to a DataFrame
## Save the Data as CSV

def fetch_crime_data(lat, lng, date):
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json()
        
    else:
        print(f"Error fetching data. Status code: {response.status_code}")
        return None
    
# Example usage: Fetch crime data for a specific location and date
if __name__ == "__main__":
    lat = 52.629729  # Latitude for the location (e.g., Nottingham, UK)
    lng = -1.131592  # Longitude for the location (e.g., Nottingham, UK)
    date = "2024-01"  # Example date (YYYY-MM format)
    
    # Fetch the crime data
    crime_data = fetch_crime_data(lat, lng, date)
    
    # If data is fetched successfully, print the first 5 results
    if crime_data:
        df = pd.DataFrame(crime_data)
        print(df.head())
        
        
        
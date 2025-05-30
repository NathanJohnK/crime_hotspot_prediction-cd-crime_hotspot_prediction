import requests
import pandas as pd
import time
import os 
import json

from imports import *


def fetch_crime_data(lat, lng, date):
    filename = f"crime_{lat}_{lng}_{date}.json"
    
    # If file already exists, load from disk
    if os.path.exists(filename):
        
        with open(filename, 'r') as f:
            data = json.load(f)
        return data

    # Otherwise, fetch from API
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        # Save to local JSON
        with open(filename, 'w') as f:
            json.dump(data, f)
        return data
    else:
        
        return None


# Example usage: Fetch crime data for a specific location and date
if __name__ == "__main__":
    lat = 52.629729  # Latitude for the location (e.g., Nottingham, UK)
    lng = -1.131592  # Longitude for the location (e.g., Nottingham, UK)
    date = "2024-01"  # Example date (YYYY-MM format)
    
    # Fetch the crime data
    crime_data = fetch_crime_data(lat, lng, date)
    
    # If data is fetched successfully, print the first 5 results
    #if crime_data:
      #print(crime_data[0])
    
    #if crime_data:
      #  df = pd.DataFrame(crime_data)
      #  print(df.head())
        
# Define multiple locations (a simple grid of points)
locations = [
    (52.9536, -1.15047),  # Nottingham
    (51.50853, -0.12574),  # London
    (53.48095, -2.23743),  # Manchester
    (55.95206, -3.19648),  # Edinburgh
]

# Define the date range (last 3 months as an example)
dates = [
    "2024-01", "2024-02", "2024-03", "2024-04", "2024-05", "2024-06",
    "2024-07", "2024-08", "2024-09", "2024-10", "2024-11", "2024-12"
]

# Store results in a list
all_crime_data = []

# Fetch data for each location and date
for lat, lng in locations:
    for date in dates:
        crime_data = fetch_crime_data(lat, lng, date)
        if crime_data:
            all_crime_data.extend(crime_data)  # Append results to the list
        time.sleep(1)  # Prevent overloading the API

# Convert to DataFrame
# df = pd.DataFrame(all_crime_data)

# Flattening the 'location' and 'outcome_status' dictionaries
# Flatten the nested fields
for record in all_crime_data:
    location = record.get('location', {})
    record['latitude'] = location.get('latitude', None)
    record['longitude'] = location.get('longitude', None)
    record.pop('location', None)
    
    outcome = record.get('outcome_status')
    if outcome:
        record['outcome_category'] = outcome.get('category', 'Unknown')
        record['outcome_date'] = outcome.get('date', 'Unknown')
    else:
        record['outcome_category'] = 'Unknown'
        record['outcome_date'] = 'Unknown'
    record.pop('outcome_status', None)

# Convert to DataFrame
df = pd.DataFrame(all_crime_data)

os.makedirs("data", exist_ok=True)  # Creates the folder if it doesn't exist
df.to_csv("data/flattened_crime_data.csv", index=False)

if not df.empty:
    print("Data fetched successfully")



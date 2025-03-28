import requests
import pandas as pd
import time

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
        
# Define multiple locations (a simple grid of points)
locations = [
    (52.629729, -1.131592),  # Nottingham
    (51.5074, -0.1278),  # London
    (53.483959, -2.244644),  # Manchester
    (55.9533, -3.1883),  # Edinburgh
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
        print(f"Fetching data for {lat}, {lng} on {date}...")
        crime_data = fetch_crime_data(lat, lng, date)
        if crime_data:
            all_crime_data.extend(crime_data)  # Append results to the list
        time.sleep(1)  # Prevent overloading the API

# Convert to DataFrame
# df = pd.DataFrame(all_crime_data)

def convert_to_df(all_crime_data):
    df = pd.DataFrame(all_crime_data)
    return df
    
# Call the function to convert the data to a DataFrame
df = convert_to_df(all_crime_data)

# Display results
print(df.info())

# Save to CSV for analysis
##df.to_csv("crime_data.csv", index=False)
#print("Crime data saved to crime_data.csv")

# Categorical summary
print(df.describe(include='all'))

# Check unique crime categories and outcomes
print(df['category'].value_counts())

# Summary statistics for the numeric 'id' column
print(df['id'].describe())
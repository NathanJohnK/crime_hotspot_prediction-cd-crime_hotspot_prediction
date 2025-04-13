import pandas as pd

# Load the existing CSV file for preprocessing
df_original = pd.read_csv("data/flattened_crime_data.csv")
df_original = df_original.sort_values(by=["location_type", "latitude", "longitude"])

# Make a copy of the DataFrame if needed
df_clean = df_original.copy()

# Basic exploration
print(f"Total records (rows): {df_clean.shape[0]}")
print(f"Total columns: {df_clean.shape[1]}")
# print(f"First 5 records:\n{df_clean.head(500)}")

# Get column names
print(df_clean.columns)
# Get summary statistics for numerical columns
# print(df_clean.describe())

## transform the coordinates

df_clean['latitude'] = pd.to_numeric(df_clean['latitude'], errors="coerce")
df_clean['longitude'] = pd.to_numeric(df_clean['longitude'], errors="coerce")


locations = [
    (52.629729, -1.131592),  # Nottingham
    (51.5074, -0.1278),      # London
    (53.483959, -2.244644),  # Manchester
    (55.9533, -3.1883),      # Edinburgh
]

locations = {
    'Nottingham': (52.629729, -1.131592),
    'London': (51.5074, -0.1278),
    'Manchester': (53.483959, -2.244644),
    'Edinburgh': (55.9533, -3.1883)
}

# Simple Euclidean distance function
def location_categorise(latitude, longitude):
    min_dist = float('inf')
    nearest_city = 'Unknown location'
    for city, (lat, lon) in locations.items():
        dist = (latitude - lat) ** 2 + (longitude - lon) ** 2  # Subtract your input latitude/longitude from the city’s values. Calculates the Euchlidian distance
        if dist < min_dist:
            min_dist = dist
            nearest_city = city
    return nearest_city

# Apply it to the DataFrame
df_clean['City'] = df_clean.apply(lambda row: location_categorise(row['latitude'], row['longitude']), axis=1)

# View output
print(df_clean[["City", "latitude", "longitude", "location_type", "location_subtype", "id"]].head(20))
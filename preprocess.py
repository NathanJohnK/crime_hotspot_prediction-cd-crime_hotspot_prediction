import pandas as pd

# Load the existing CSV file for preprocessing
df_original = pd.read_csv("data/flattened_crime_data.csv")

# Preprocessing steps (e.g., sorting)
df_original = df_original.sort_values(by=["location_type", "latitude", "longitude"])

# Make a copy of the DataFrame if needed
df_clean = df_original.copy()

# Basic exploration
# print(f"Total records (rows): {df_clean.shape[0]}")
# print(f"Total columns: {df_clean.shape[1]}")
# print(f"First 5 records:\n{df_clean.head(500)}")

# Get column names
# print(df_clean.columns)
# Get summary statistics for numerical columns
# print(df_clean.describe())

## transform the coordinates

df_clean['latitude'] = pd.to_numeric(df_clean['latitude'], errors="coerce")
df_clean['longitude'] = pd.to_numeric(df_clean['longitude'], errors="coerce")

print(df_clean[["location_type", "latitude", "longitude"]].head(20))


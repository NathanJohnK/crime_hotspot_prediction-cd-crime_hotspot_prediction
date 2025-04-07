from imports import *  # Import everything from imports.py
from fetch_data import all_crime_data

df = pd.read_csv("data/flattened_crime_data.csv")
df = df.sort_values(by=["category", "location_type"])
print(df.head(10))

df.describe()
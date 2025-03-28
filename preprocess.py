from imports import *  # Import everything from imports.py
from fetch_data import convert_to_df
from fetch_data import all_crime_data

df = convert_to_df(all_crime_data)

# Categorical summary
df.sort_values(by =["category", "location_type"])

print(df.head(10))  # Show first 10 rows
from imports import *  # Import everything from imports.py
from fetch_data import all_crime_data

df_original = pd.read_csv("data/flattened_crime_data.csv")
df_original = df_original.sort_values(by=["category", "location_type"])
print(df_original.head(10))

df_original.describe()

df_clean = df_original.copy()



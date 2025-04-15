
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.pyplot as plt
import seaborn as sns


# Load the DataFrame

Visual_df = pd.read_csv('Cleaned_df.csv')

notts_df = Visual_df[Visual_df['City'] == 'Nottingham']
print(notts_df[['latitude', 'longitude']].describe())



import pandas as pd

top_n = 10
city = "London"

city_df = Visual_df[Visual_df['City'] == city]
top_crimes = city_df['category'].value_counts().nlargest(top_n)

# Create a new DataFrame for Seaborn
plot_df = pd.DataFrame({
    'category': top_crimes.index,
    'count': top_crimes.values
})

plt.figure(figsize=(10, 6))
sns.barplot(data=plot_df, y='category', x='count', hue='category', palette='viridis', legend=False)
plt.title(f"Top {top_n} Crimes in {city}")
plt.xlabel("Number of Incidents")
plt.ylabel("Crime Type")
plt.tight_layout()
#plt.show()


import seaborn as sns

import matplotlib.pyplot as plt
import seaborn as sns

plt.clf()

notts_df = Visual_df[Visual_df['City'] == 'Nottingham']

import geopandas as gpd
from shapely.geometry import Point

# Filter to Nottingham
notts_df = Visual_df[Visual_df['City'] == 'Nottingham'].copy()

# Create geometry column
notts_df['geometry'] = notts_df.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

# Convert to GeoDataFrame and set coordinate system (WGS84)
gdf = gpd.GeoDataFrame(notts_df, geometry='geometry', crs='EPSG:4326')

# Convert to Web Mercator for contextily (tile background)
gdf = gdf.to_crs(epsg=3857)

import matplotlib.pyplot as plt
import contextily as ctx

fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, column='category', legend=True, markersize=10, alpha=0.6)

ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
ax.set_title("Nottingham Crime Map with Real Basemap")
plt.axis('off')
#plt.show()
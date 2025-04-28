
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as ctx
import geopandas as gpd
from shapely.geometry import Point
import matplotlib.pyplot as plt
import contextily as ctx

# Load the DataFrame

Visual_df = pd.read_csv('Cleaned_df.csv')

def top_10_records(city, df):
    city_visual_df = df[df['City'] == city]
    top_n = 10
    city_df = Visual_df[Visual_df['City'] == city]
    top_crimes = city_visual_df['category'].value_counts().nlargest(top_n)

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
    plt.show()
# top_10_records("Nottingham", Visual_df)

plt.clf()

def graphs(city, df, top_n):
    # Filter by city
    city_visual_df = df[df['City'] == city]

    # Get top N crime categories
    top_crimes = city_visual_df['category'].value_counts().nlargest(top_n).index

    # Keep only rows where the crime is in the top N
    city_visual_df = city_visual_df[city_visual_df['category'].isin(top_crimes)]

    # Create geometry column
    city_visual_df['geometry'] = city_visual_df.apply(lambda row: Point(row['longitude'], row['latitude']), axis=1)

    # Convert to GeoDataFrame and project
    gdf = gpd.GeoDataFrame(city_visual_df, geometry='geometry', crs="EPSG:4326")
    gdf = gdf.to_crs(epsg=3857)

    # Plot
    fig, ax = plt.subplots(figsize=(10, 10))
    gdf.plot(ax=ax, column='category', legend=True, markersize=10, alpha=0.6)
    ctx.add_basemap(ax, source=ctx.providers.OpenStreetMap.Mapnik)
    ax.set_title(f"{city} - Top {top_n} Crimes")
    plt.axis('off')
    plt.show()
    
graphs("Nottingham", Visual_df, top_n=1)

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn import preprocessing
import seaborn as sns
import contextily as ctx  # add this if you don't have it yet: pip install contextily
import geopandas as gpd
from shapely.geometry import Point



# Assuming 'Visual_df' is DataFrame with 'latitude' and 'longitude' columns
# Replace this if needed with your actual df
# Visual_df = pd.read_csv('your_data.csv')
Visual_df = pd.read_csv('Cleaned_df.csv')

# Slice dataframe to the relevant city

def city_for_model(city):
    city_df = Visual_df[Visual_df['City'] == city]
    return city_df

# Extract latitude and longitude values from revised df

new_df = city_for_model("Nottingham")

X = new_df[['latitude', 'longitude']].values

# Number of clusters (adjust as needed)
k = 6  # You can change this number depending on your needs

# Fit the KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# 1. Normalize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Get cluster centers (optional)
centers = kmeans.cluster_centers_

# Add the cluster labels to the dataframe
new_df['cluster'] = kmeans.labels_

inertia = []
silhouette_scores = []
cluster_range = range(2, 11)  # Trying 2 to 10 clusters

for n_clusters in cluster_range:
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    labels = kmeans.fit_predict(X_scaled)
    inertia.append(kmeans.inertia_)
    silhouette = silhouette_score(X_scaled, labels)
    silhouette_scores.append(silhouette)

# Plotting the Elbow Plot (Inertia)
plt.figure(figsize=(12, 5))

plt.subplot(1, 2, 1)
plt.plot(cluster_range, inertia, marker='o')
plt.title('Elbow Method (Inertia)')
plt.xlabel('Number of Clusters')
plt.ylabel('Inertia')

# Plotting the Silhouette Scores
plt.subplot(1, 2, 2)
plt.plot(cluster_range, silhouette_scores, marker='o', color='green')
plt.title('Silhouette Scores')
plt.xlabel('Number of Clusters')
plt.ylabel('Silhouette Score')

plt.tight_layout()
#plt.show()

# Display the clusters
#print(Visual_df)

# Step 1: Create a GeoDataFrame from your latitude/longitude
geometry = [Point(xy) for xy in zip(new_df['longitude'], new_df['latitude'])]
geo_df = gpd.GeoDataFrame(new_df, geometry=geometry, crs="EPSG:4326")

# Step 2: Project to Web Mercator for plotting with a basemap
geo_df = geo_df.to_crs(epsg=3857)

# Also transform the centers
centers_df = pd.DataFrame(centers, columns=['latitude', 'longitude'])
centers_geometry = [Point(xy) for xy in zip(centers_df['longitude'], centers_df['latitude'])]
centers_geo = gpd.GeoDataFrame(centers_df, geometry=centers_geometry, crs="EPSG:4326").to_crs(epsg=3857)

# Step 3: Plot
fig, ax = plt.subplots(figsize=(10, 10))
geo_df.plot(ax=ax, column='cluster', cmap='viridis', legend=True, markersize=20)
centers_geo.plot(ax=ax, color='red', marker='X', markersize=100, label='Centroids')

# Add basemap
ctx.add_basemap(ax, source=ctx.providers.CartoDB.Positron)

# Step 4: Add cluster labels near centroids
for i, row in centers_df.iterrows():
    ax.text(
        x=row['longitude'], y=row['latitude'],  # Position of the label
        s=f"Cluster {i}",  # Label text
        color='black', fontsize=12, fontweight='bold', 
        ha='center', va='center', 
        backgroundcolor='white', alpha=0.7)  # Label styling

# Styling
plt.title('K-Means Clustering in Nottingham')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.legend()
plt.show()

#print(new_df.columns)

# Create a color map for crime types
crime_type_colors = {crime: plt.cm.viridis(i / len(new_df['category'].unique())) for i, crime in enumerate(new_df['category'].unique())}

# Plot the data, coloring by crime type
plt.figure(figsize=(10, 6))
for crime, color in crime_type_colors.items():
    subset = new_df[new_df['category'] == crime]
    plt.scatter(subset['longitude'], subset['latitude'], color=color, label=crime, alpha=0.6)

plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('Crime Types Distribution by Location')
plt.legend(loc='upper right')
plt.show()

# Group by cluster and crime type, then count occurrences
crime_counts = new_df.groupby(['cluster', 'category']).size().unstack(fill_value=0)

# Display the result
print(crime_counts)

# Total number of crimes per cluster

total_crimes_per_cluster = new_df.groupby('cluster').size().reset_index(name='crime_count')

# Plot
# plt.figure(figsize=(8, 5))
# sns.barplot(data=total_crimes_per_cluster, x='cluster', y='crime_count', palette='viridis')

# plt.title('Number of Crimes per Cluster')
# plt.xlabel('Cluster')
# plt.ylabel('Crime Count')
# plt.tight_layout()
# plt.show()

# Group by cluster and crime type, then count
crime_counts = new_df.groupby(['cluster', 'category']).size().unstack(fill_value=0)

# Plot grouped bar chart
crime_counts.plot(kind='bar', stacked=False, figsize=(12, 6), colormap='viridis')

plt.title('Crime Type Distribution per Cluster')
plt.xlabel('Cluster')
plt.ylabel('Number of Crimes')
plt.legend(title='Crime Type', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.tight_layout()
plt.show()
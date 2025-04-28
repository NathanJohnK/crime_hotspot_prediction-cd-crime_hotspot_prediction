import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from kneed import KneeLocator
from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score
from sklearn.preprocessing import StandardScaler

# Assuming 'Visual_df' is DataFrame with 'latitude' and 'longitude' columns
# Replace this if needed with your actual df
# Visual_df = pd.read_csv('your_data.csv')
Visual_df = pd.read_csv('Cleaned_df.csv')

#Slice dataframe to the relevant city

    """
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
        """

def city_for_model():
    
    




# Extract latitude and longitude values from Visual_df
X = Visual_df[['latitude', 'longitude']].values

# Number of clusters (adjust as needed)
k = 3  # You can change this number depending on your needs

# Fit the KMeans model
kmeans = KMeans(n_clusters=k, random_state=42)
kmeans.fit(X)

# Get cluster centers (optional)
centers = kmeans.cluster_centers_

# Add the cluster labels to the dataframe
Visual_df['cluster'] = kmeans.labels_

# Display the clusters
#print(Visual_df)

# Plotting the results (optional)
plt.scatter(Visual_df['longitude'], Visual_df['latitude'], c=Visual_df['cluster'], cmap='viridis')
plt.scatter(centers[:, 1], centers[:, 0], c='red', marker='X', label='Centroids')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('K-Means Clustering (Latitude and Longitude)')
plt.legend()
#plt.show()
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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
print(Visual_df)

# Plotting the results (optional)
plt.scatter(Visual_df['longitude'], Visual_df['latitude'], c=Visual_df['cluster'], cmap='viridis')
plt.scatter(centers[:, 1], centers[:, 0], c='red', marker='X', label='Centroids')
plt.xlabel('Longitude')
plt.ylabel('Latitude')
plt.title('K-Means Clustering (Latitude and Longitude)')
plt.legend()
plt.show()
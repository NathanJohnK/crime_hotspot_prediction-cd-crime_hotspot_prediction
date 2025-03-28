# Core Data Processing
import pandas as pd
import numpy as np

# Geospatial Analysis
import geopandas as gpd
from shapely.geometry import Point, Polygon
import folium
from geopy.geocoders import Nominatim

# Data Cleaning & Feature Engineering
import re
from dateutil import parser
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score  # To evaluate clustering performance

# Big Data Handling
import dask.dataframe as dd
import polars as pl

# Visualization
import matplotlib.pyplot as plt
import seaborn as sns
import scipy
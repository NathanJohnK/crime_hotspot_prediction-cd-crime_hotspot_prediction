import unittest
from unittest.mock import patch
import requests
from fetch_data import fetch_crime_data   # Import the function from your script
import pandas as pd
#from fetch_data import convert_to_df
from preprocess import df_original 
from preprocess import df_clean
from train_model import city_for_model

def test_fetch_crime_data():
    lat = 52.629729  # Latitude for the location (e.g., Nottingham, UK)
    lng = -1.131592  # Longitude for the location (e.g., Nottingham, UK)
    date = "2024-01"  # Example date (YYYY-MM format)
    
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"
    
    # Send a request to the API
    response = requests.get(url)
    
    # Assert that the response status code is 200 (OK)
    assert response.status_code == 200
    print(f"Response status code: {response.status_code}")  # To see the status code in the output
    

def test_json_being_produced():
    lat = 52.629729  # Latitude for the location (e.g., Nottingham, UK)
    lng = -1.131592  # Longitude for the location (e.g., Nottingham, UK)
    date = "2024-01"  # Example date (YYYY-MM format)
    
    url = f"https://data.police.uk/api/crimes-street/all-crime?date={date}&lat={lat}&lng={lng}"
    response = requests.get(url)
    # Assert that the response is in JSON format by checking the content type
    assert response.headers["Content-Type"].startswith("application/json")
    
def test_dataframe_creation():
    lat = 52.629729  # Latitude for the location (e.g., Nottingham, UK)
    lng = -1.131592  # Longitude for the location (e.g., Nottingham, UK)
    date = "2024-01"  # Example date (YYYY-MM format)
    
    crime_data = fetch_crime_data(lat, lng, date)
    assert crime_data is not None, "No crime data returned"
    
    # Create DataFrame
    df = pd.DataFrame(crime_data)
    
    # Check if the DataFrame is created correctly
    assert isinstance(df, pd.DataFrame), "The data is not a DataFrame"
    
    # Check if the DataFrame is not empty
    assert not df.empty, "The DataFrame is empty"
    
    #check that
    
    ### tests for pre process

###test to check df copied correctly

def test_df_is_not_empty():
    assert isinstance(df_clean, pd.DataFrame), "The data is not a DataFrame"
    assert not df_clean.empty, 'df empty'

def test_dataframe_copy():
    df_original = pd.read_csv("data/flattened_crime_data.csv")
    df_clean = df_original.copy()
    assert df_original.equals(df_clean), "The copied dataframe should be identical to the original"

def test_city_returns_filtered_df():
    Visual_df = pd.read_csv('Cleaned_df.csv')
    new_df = city_for_model("Nottingham")
    assert not new_df.equals(Visual_df), "New DataFrame should be different from original"
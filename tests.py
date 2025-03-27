import unittest
from unittest.mock import patch
import requests
from fetch_data import fetch_crime_data  # Import the function from your script
import pandas as pd


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
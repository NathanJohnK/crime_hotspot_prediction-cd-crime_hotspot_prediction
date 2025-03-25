import unittest
import requests
from unittest.mock import patch
from fetch_data import fetch_crime_data  # Import the function from your script

class TestFetchCrimeData(unittest.TestCase):

    @patch("fetch_data.requests.get")  # Mock the API request
    def test_fetch_crime_data_success(self, mock_get):
        """Test if function returns JSON data on successful API call"""
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = [{"category": "burglary"}]

        result = fetch_crime_data(52.629729, -1.131592, "2024-01")
        self.assertIsInstance(result, list)  # Ensure result is a list
        self.assertGreater(len(result), 0)  # Ensure it has data
        self.assertIn("category", result[0])  # Check for expected keys

    @patch("fetch_data.requests.get")
    def test_fetch_crime_data_failure(self, mock_get):
        """Test if function handles failed API calls properly"""
        mock_get.return_value.status_code = 400
        result = fetch_crime_data(52.629729, -1.131592, "2024-01")
        self.assertIsNone(result)  # Function should return None on failure

if __name__ == "__main__":
    unittest.main()
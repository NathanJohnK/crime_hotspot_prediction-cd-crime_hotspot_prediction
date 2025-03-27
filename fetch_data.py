import requests
import pandas as pd

url = f"https://data.police.uk/api/crimes-street/all-crime?lat={lat}&lng={lng}&date={date}"

## API request
#Convert Data to a DataFrame
## Save the Data as CSV
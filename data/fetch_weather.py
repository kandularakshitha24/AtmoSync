import requests
import pandas as pd
from pathlib import Path

# Hyderabad coordinates
latitude = 17.3850
longitude = 78.4867

# Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast"

params = {
	"latitude": latitude,
	"longitude": longitude,
	"hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
	"timezone": "auto",
}

# Send request to the API
response = requests.get(url, params=params)

# Check whether the request was successful
if response.status_code == 200:
	data = response.json()

	# Convert hourly weather data into a DataFrame
	df = pd.DataFrame(data["hourly"])

	print("Weather data collected successfully!")
	print(df.head())

	# Save CSV inside the data folder
	output_path = Path(__file__).parent / "weather_data.csv"
	df.to_csv(output_path, index=False)

	print(f"Weather data saved to: {output_path}")
else:
	print("Failed to collect weather data.")
	print("Status code:", response.status_code)

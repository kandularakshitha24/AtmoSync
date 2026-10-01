import requests
import pandas as pd
from pathlib import Path

# Multiple locations around Hyderabad
locations = {
	"Hyderabad_Central": (17.3850, 78.4867),
	"HITEC_City": (17.4435, 78.3772),
	"Secunderabad": (17.4399, 78.4983),
	"Gachibowli": (17.4401, 78.3489),
}

# Open-Meteo API
url = "https://api.open-meteo.com/v1/forecast"
all_data = []

# Collect weather data for each location
for location_name, (latitude, longitude) in locations.items():
	params = {
		"latitude": latitude,
		"longitude": longitude,
		"hourly": "temperature_2m,relative_humidity_2m,precipitation,wind_speed_10m",
		"timezone": "auto",
	}

	print(f"\nCollecting weather data for {location_name}...")

	try:
		response = requests.get(url, params=params, timeout=30)
		response.raise_for_status()
		data = response.json()

		# Convert hourly data into a DataFrame and label its location.
		df = pd.DataFrame(data["hourly"])
		df["location"] = location_name
		all_data.append(df)
		print(f"{location_name} data collected successfully!")
	except (requests.RequestException, ValueError, KeyError) as error:
		print(f"Failed to collect data for {location_name}: {error}")

# Combine and save the data collected successfully.
if all_data:
	combined_df = pd.concat(all_data, ignore_index=True)

	print("\nAll location data combined successfully!")
	print("Total rows:", len(combined_df))
	print("Total columns:", len(combined_df.columns))
	print("\nLocations collected:")
	print(combined_df["location"].unique())
	print("\nFirst 5 rows:")
	print(combined_df.head())

	output_path = Path(__file__).parent / "multi_location_weather.csv"
	combined_df.to_csv(output_path, index=False)
	print("\nMulti-location weather data saved successfully!")
	print("Saved to:", output_path)
else:
	print("\nNo weather data was collected.")

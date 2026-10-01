import pandas as pd
from pathlib import Path

# Load the multi-location weather dataset
input_path = Path(__file__).parent / "multi_location_weather.csv"

df = pd.read_csv(input_path)

print("Multi-location weather data loaded successfully!")


# -------------------------------
# Calculate location averages
# -------------------------------

location_summary = df.groupby("location").agg(
	average_temperature=("temperature_2m", "mean"),
	average_humidity=("relative_humidity_2m", "mean"),
	average_wind_speed=("wind_speed_10m", "mean")
).reset_index()


# -------------------------------
# Calculate overall averages
# -------------------------------

overall_temperature = df["temperature_2m"].mean()
overall_humidity = df["relative_humidity_2m"].mean()
overall_wind_speed = df["wind_speed_10m"].mean()


# -------------------------------
# Calculate differences
# -------------------------------

location_summary["temperature_difference"] = (
	location_summary["average_temperature"]
	- overall_temperature
)

location_summary["humidity_difference"] = (
	location_summary["average_humidity"]
	- overall_humidity
)

location_summary["wind_difference"] = (
	location_summary["average_wind_speed"]
	- overall_wind_speed
)


# -------------------------------
# Display results
# -------------------------------

print("\nMicro-climate indicators:")
print(location_summary.to_string(index=False))


# -------------------------------
# Save results
# -------------------------------

output_path = Path(__file__).parent / "microclimate_indicators.csv"

location_summary.to_csv(
	output_path,
	index=False
)

print("\nMicro-climate indicators saved successfully!")
print("Saved to:", output_path)

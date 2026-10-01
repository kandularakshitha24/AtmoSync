import pandas as pd
from pathlib import Path


# Load the multi-location weather dataset.
data_dir = Path(__file__).parent
input_path = data_dir / "multi_location_weather.csv"
df = pd.read_csv(input_path)

print("Multi-location weather data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))


# Summarize temperature by location.
temperature_summary = df.groupby("location")["temperature_2m"].agg(
	["mean", "min", "max"]
).reset_index()
temperature_summary.columns = [
	"location",
	"average_temperature",
	"minimum_temperature",
	"maximum_temperature",
]
temperature_summary["temperature_range"] = (
	temperature_summary["maximum_temperature"]
	- temperature_summary["minimum_temperature"]
)
print("\nTemperature comparison:")
print(temperature_summary.to_string(index=False))


# Summarize humidity by location.
humidity_summary = df.groupby("location")["relative_humidity_2m"].agg(
	["mean", "min", "max"]
).reset_index()
humidity_summary.columns = [
	"location",
	"average_humidity",
	"minimum_humidity",
	"maximum_humidity",
]
print("\nHumidity comparison:")
print(humidity_summary.to_string(index=False))


# Summarize wind speed by location.
wind_summary = df.groupby("location")["wind_speed_10m"].agg(
	["mean", "min", "max"]
).reset_index()
wind_summary.columns = [
	"location",
	"average_wind_speed",
	"minimum_wind_speed",
	"maximum_wind_speed",
]
print("\nWind speed comparison:")
print(wind_summary.to_string(index=False))


# Save each analysis summary alongside the source data.
temperature_output = data_dir / "microclimate_temperature_summary.csv"
humidity_output = data_dir / "microclimate_humidity_summary.csv"
wind_output = data_dir / "microclimate_wind_summary.csv"

temperature_summary.to_csv(temperature_output, index=False)
humidity_summary.to_csv(humidity_output, index=False)
wind_summary.to_csv(wind_output, index=False)

print("\nMicro-climate analysis files saved successfully!")
print("Temperature:", temperature_output)
print("Humidity:", humidity_output)
print("Wind:", wind_output)

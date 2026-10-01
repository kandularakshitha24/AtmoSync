import pandas as pd
from pathlib import Path

# Load the processed weather dataset
input_path = Path(__file__).parent / "processed_weather_data.csv"

df = pd.read_csv(input_path)

print("Processed weather data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFirst 5 rows:")
print(df.head())
# Convert time column to datetime
df["time"] = pd.to_datetime(df["time"])

# Create time-based features
df["hour"] = df["time"].dt.hour
df["day"] = df["time"].dt.day
df["month"] = df["time"].dt.month
df["day_of_week"] = df["time"].dt.dayofweek

print("\nTime-based features created successfully!")
print(df[[
    "time",
    "hour",
    "day",
    "month",
    "day_of_week"
]].head())
# Create weather-change features
df["temperature_change"] = df["temperature_2m"].diff()
df["humidity_change"] = df["relative_humidity_2m"].diff()
df["wind_speed_change"] = df["wind_speed_10m"].diff()

print("\nWeather-change features created successfully!")

print(df[[
    "time",
    "temperature_2m",
    "temperature_change",
    "relative_humidity_2m",
    "humidity_change",
    "wind_speed_10m",
    "wind_speed_change"
]].head())
# Check missing values created by feature engineering
print("\nMissing values after feature creation:")
print(df.isnull().sum())

# Remove the first row because it has no previous hour
df = df.dropna().reset_index(drop=True)

print("\nFirst row with missing change values removed.")
print("Rows after removing NaN:", len(df))
# Save the feature-engineered dataset
output_path = Path(__file__).parent / "feature_engineered_weather.csv"

df.to_csv(output_path, index=False)

print("\nFeature-engineered weather data saved successfully!")
print("Saved to:", output_path)
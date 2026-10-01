import pandas as pd
from pathlib import Path

# Load the weather dataset
input_path = Path(__file__).parent / "weather_data.csv"

df = pd.read_csv(input_path)

print("Weather data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

print("\nFirst 5 rows:")
print(df.head())
print("\nMissing values:")
print(df.isnull().sum())
print("\nDuplicate rows:", df.duplicated().sum())
df["time"] = pd.to_datetime(df["time"])

print("\nTime column converted successfully!")
print("Time data type:", df["time"].dtype)
df = df.sort_values("time").reset_index(drop=True)

print("\nData sorted by time successfully!")
print(df.head())
# Save the processed dataset
output_path = Path(__file__).parent / "processed_weather_data.csv"

df.to_csv(output_path, index=False)

print("\nProcessed weather data saved successfully!")
print("Saved to:", output_path)
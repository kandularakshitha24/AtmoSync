import pandas as pd
from pathlib import Path

# Load micro-climate indicators
input_path = Path(__file__).parent / "microclimate_indicators.csv"
df = pd.read_csv(input_path)

print("Micro-climate indicators loaded successfully!")

# Find locations with highest and lowest values
metrics = (
	("average_temperature", "temperature", "°C"),
	("average_humidity", "humidity", "%"),
	("average_wind_speed", "wind speed", "km/h"),
)

insights = []
for column, label, unit in metrics:
	highest = df.loc[df[column].idxmax()]
	lowest = df.loc[df[column].idxmin()]
	insights.append(
		f"{highest['location']} has the highest average {label} "
		f"of {highest[column]:.2f} {unit}."
	)
	insights.append(
		f"{lowest['location']} has the lowest average {label} "
		f"of {lowest[column]:.2f} {unit}."
	)

print("\nLocalized Micro-Climate Insights:")
print("----------------------------------")
for i, insight in enumerate(insights, start=1):
	print(f"{i}. {insight}")

output_path = Path(__file__).parent / "microclimate_insights.txt"
with open(output_path, "w", encoding="utf-8") as file:
	file.write("AtmoSync - Localized Micro-Climate Insights\n")
	file.write("=" * 50 + "\n\n")
	for i, insight in enumerate(insights, start=1):
		file.write(f"{i}. {insight}\n")

print("\nMicro-climate insights saved successfully!")
print("Saved to:", output_path)

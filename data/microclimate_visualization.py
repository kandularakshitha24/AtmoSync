import pandas as pd
import matplotlib.pyplot as plt
from pathlib import Path

# Load micro-climate indicators
input_path = Path(__file__).parent / "microclimate_indicators.csv"
df = pd.read_csv(input_path)

print("Micro-climate indicators loaded successfully!")


def create_bar_chart(column, title, ylabel, output_filename):
    """Create and save a bar chart for one micro-climate indicator."""
    plt.figure(figsize=(8, 5))
    plt.bar(df["location"], df[column])
    plt.title(title)
    plt.xlabel("Location")
    plt.ylabel(ylabel)
    plt.xticks(rotation=20)
    plt.tight_layout()

    output_path = Path(__file__).parent / output_filename
    plt.savefig(output_path)
    plt.show()
    plt.close()
    print(f"{title} graph saved!")


create_bar_chart(
    "average_temperature",
    "Average Temperature by Location",
    "Temperature (°C)",
    "temperature_comparison.png",
)

create_bar_chart(
    "average_humidity",
    "Average Humidity by Location",
    "Humidity (%)",
    "humidity_comparison.png",
)

create_bar_chart(
    "average_wind_speed",
    "Average Wind Speed by Location",
    "Wind Speed (km/h)",
    "wind_comparison.png",
)

print("\nAll micro-climate visualizations created successfully!")
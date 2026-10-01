import streamlit as st
import requests
import pandas as pd
import plotly.express as px

# Page configuration
st.set_page_config(
    page_title="AtmoSync",
    page_icon="🌦️",
    layout="wide"
)

# FastAPI backend URL
API_URL = "http://127.0.0.1:8000/microclimate"

# Get micro-climate data from FastAPI
response = requests.get(API_URL)

if response.status_code == 200:
    microclimate_data = response.json()
else:
    st.error("Unable to connect to FastAPI backend.")
    microclimate_data = []

# Title
st.title("🌦️ AtmoSync")
st.subheader("Micro-Climate Arbitrage Analytics")

st.write(
    "Analyze localized weather conditions and generate "
    "micro-climate insights."
)

# Use Hyderabad Central as the dashboard summary
summary_data = next(
    item for item in microclimate_data
    if item["location"] == "Hyderabad_Central"
)

# Dashboard metrics
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(
        label="🌡️ Average Temperature",
        value=f"{summary_data['average_temperature']:.1f} °C"
    )

with col2:
    st.metric(
        label="💧 Average Humidity",
        value=f"{summary_data['average_humidity']:.1f}%"
    )

with col3:
    st.metric(
        label="💨 Average Wind Speed",
        value=f"{summary_data['average_wind_speed']:.2f} km/h"
    )

st.divider()

# Micro-climate locations
st.header("📍 Micro-Climate Locations")

locations = [
    item["location"]
    for item in microclimate_data
]

selected_location = st.selectbox(
    "Select a location",
    locations
)

# Get data for selected location
selected_data = next(
    item for item in microclimate_data
    if item["location"] == selected_location
)

st.write(
    f"Selected location: **{selected_location}**"
)

st.write(
    f"🌡️ Temperature: **{selected_data['average_temperature']:.2f} °C**"
)

st.write(
    f"💧 Humidity: **{selected_data['average_humidity']:.2f}%**"
)

st.write(
    f"💨 Wind Speed: **{selected_data['average_wind_speed']:.2f} km/h**"
)
# Temperature comparison chart
# Temperature comparison chart
st.header("🌡️ Average Temperature Comparison")

temperature_chart_data = pd.DataFrame(
    microclimate_data
)

temperature_fig = px.bar(
    temperature_chart_data,
    x="location",
    y="average_temperature",
    title="Average Temperature by Location",
    labels={
        "location": "Location",
        "average_temperature": "Temperature (°C)"
    }
)

temperature_fig.update_layout(
    xaxis_tickangle=-20
)

st.plotly_chart(
    temperature_fig,
    use_container_width=True
)

# Humidity comparison chart
# Humidity comparison chart
st.header("💧 Average Humidity Comparison")

humidity_fig = px.bar(
    temperature_chart_data,
    x="location",
    y="average_humidity",
    title="Average Humidity by Location",
    labels={
        "location": "Location",
        "average_humidity": "Humidity (%)"
    }
)

humidity_fig.update_layout(
    xaxis_tickangle=-20
)

st.plotly_chart(
    humidity_fig,
    use_container_width=True
)
# Wind speed comparison chart
# Wind speed comparison chart
st.header("💨 Average Wind Speed Comparison")

wind_fig = px.bar(
    temperature_chart_data,
    x="location",
    y="average_wind_speed",
    title="Average Wind Speed by Location",
    labels={
        "location": "Location",
        "average_wind_speed": "Wind Speed (km/h)"
    }
)

wind_fig.update_layout(
    xaxis_tickangle=-20
)

st.plotly_chart(
    wind_fig,
    use_container_width=True
)

# Next-hour temperature prediction
st.header("🤖 Next-Hour Temperature Prediction")

st.write(
    "Enter the current weather conditions to predict "
    "the temperature for the next hour."
)

col1, col2 = st.columns(2)

with col1:
    temperature = st.number_input(
        "Current Temperature (°C)",
        value=30.0
    )

    humidity = st.number_input(
        "Relative Humidity (%)",
        value=50.0
    )

    precipitation = st.number_input(
        "Precipitation (mm)",
        value=0.0
    )

    wind_speed = st.number_input(
        "Wind Speed (km/h)",
        value=8.0
    )

    hour = st.number_input(
        "Hour",
        min_value=0,
        max_value=23,
        value=15
    )

with col2:
    day = st.number_input(
        "Day",
        min_value=1,
        max_value=31,
        value=1
    )

    month = st.number_input(
        "Month",
        min_value=1,
        max_value=12,
        value=10
    )

    day_of_week = st.number_input(
        "Day of Week",
        min_value=0,
        max_value=6,
        value=3
    )

    temperature_change = st.number_input(
        "Temperature Change (°C)",
        value=0.5
    )

    humidity_change = st.number_input(
        "Humidity Change (%)",
        value=-2.0
    )

    wind_speed_change = st.number_input(
        "Wind Speed Change (km/h)",
        value=1.0
    )

if st.button("🔮 Predict Next-Hour Temperature"):

    prediction_data = {
        "temperature_2m": temperature,
        "relative_humidity_2m": humidity,
        "precipitation": precipitation,
        "wind_speed_10m": wind_speed,
        "hour": hour,
        "day": day,
        "month": month,
        "day_of_week": day_of_week,
        "temperature_change": temperature_change,
        "humidity_change": humidity_change,
        "wind_speed_change": wind_speed_change
    }

    prediction_response = requests.post(
        "http://127.0.0.1:8000/predict",
        json=prediction_data
    )

    if prediction_response.status_code == 200:

        prediction_result = prediction_response.json()

        predicted_temperature = prediction_result[
            "predicted_next_hour_temperature"
        ]

        st.success(
            f"🌡️ Predicted Next-Hour Temperature: "
            f"{predicted_temperature:.2f} °C"
        )

    else:
        st.error("Unable to get prediction from FastAPI backend.")
        # Micro-climate insights
st.header("💡 Micro-Climate Insights")

st.write(
    "The following insights are generated from the "
    "micro-climate analysis of the selected locations."
)

# Find locations with highest and lowest values
highest_temperature = max(
    microclimate_data,
    key=lambda x: x["average_temperature"]
)

lowest_temperature = min(
    microclimate_data,
    key=lambda x: x["average_temperature"]
)

highest_humidity = max(
    microclimate_data,
    key=lambda x: x["average_humidity"]
)

highest_wind = max(
    microclimate_data,
    key=lambda x: x["average_wind_speed"]
)

st.info(
    f"🌡️ **Highest average temperature:** "
    f"{highest_temperature['location']} "
    f"({highest_temperature['average_temperature']:.2f} °C)"
)

st.info(
    f"❄️ **Lowest average temperature:** "
    f"{lowest_temperature['location']} "
    f"({lowest_temperature['average_temperature']:.2f} °C)"
)

st.info(
    f"💧 **Highest average humidity:** "
    f"{highest_humidity['location']} "
    f"({highest_humidity['average_humidity']:.2f}%)"
)

st.info(
    f"💨 **Highest average wind speed:** "
    f"{highest_wind['location']} "
    f"({highest_wind['average_wind_speed']:.2f} km/h)"
)
st.success("AtmoSync dashboard is running successfully!")
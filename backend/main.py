from fastapi import FastAPI
from pydantic import BaseModel
from pathlib import Path
import joblib
import pandas as pd

app = FastAPI(
	title="AtmoSync API",
	description="Micro-Climate Arbitrage Analytics API",
	version="1.0.0"
)


# Load the trained weather prediction model
model_path = Path(__file__).parent.parent / "ml" / "weather_model.pkl"

model = joblib.load(model_path)
# Load micro-climate indicators
microclimate_path = (
    Path(__file__).parent.parent
    / "data"
    / "microclimate_indicators.csv"
)

microclimate_df = pd.read_csv(microclimate_path)

print("Micro-climate indicators loaded successfully!")
class WeatherInput(BaseModel):
    temperature_2m: float
    relative_humidity_2m: float
    precipitation: float
    wind_speed_10m: float
    hour: int
    day: int
    month: int
    day_of_week: int
    temperature_change: float
    humidity_change: float
    wind_speed_change: float

print("Weather prediction model loaded successfully!")


@app.get("/")
def home():
	return {
		"message": "Welcome to AtmoSync API",
		"status": "Backend is running"
	}
@app.post("/predict")
def predict_weather(weather: WeatherInput):

    input_data = [[
        weather.temperature_2m,
        weather.relative_humidity_2m,
        weather.precipitation,
        weather.wind_speed_10m,
        weather.hour,
        weather.day,
        weather.month,
        weather.day_of_week,
        weather.temperature_change,
        weather.humidity_change,
        weather.wind_speed_change
    ]]

    prediction = model.predict(input_data)

    return {
        "predicted_next_hour_temperature": float(prediction[0])
    }

@app.get("/microclimate")
def get_microclimate():
    return microclimate_df.to_dict(orient="records")

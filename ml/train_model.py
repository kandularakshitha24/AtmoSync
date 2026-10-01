import pandas as pd
from pathlib import Path

# Load the feature-engineered dataset
input_path = Path(__file__).parent.parent / "data" / "feature_engineered_weather.csv"

df = pd.read_csv(input_path)

print("Feature-engineered weather data loaded successfully!")
print("Rows:", len(df))
print("Columns:", len(df.columns))

# Create the target variable
# The target is the temperature of the next hour
df["next_hour_temperature"] = df["temperature_2m"].shift(-1)

print("\nTarget variable created successfully!")

print(df[[
	"time",
	"temperature_2m",
	"next_hour_temperature"
]].head())
# Remove the final row because it has no next-hour temperature
df = df.dropna(subset=["next_hour_temperature"]).reset_index(drop=True)

# Select input features
features = [
    "temperature_2m",
    "relative_humidity_2m",
    "precipitation",
    "wind_speed_10m",
    "hour",
    "day",
    "month",
    "day_of_week",
    "temperature_change",
    "humidity_change",
    "wind_speed_change"
]

X = df[features]

# Select target
y = df["next_hour_temperature"]

print("\nFeatures (X) and target (y) created successfully!")
print("X shape:", X.shape)
print("y shape:", y.shape)

print("\nFeatures used:")
print(features)

print("\nTarget:")
print("next_hour_temperature")
# Split the data chronologically into training and testing sets
split_index = int(len(X) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nData split completed successfully!")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
# Split the data chronologically into training and testing sets
split_index = int(len(X) * 0.8)

X_train = X.iloc[:split_index]
X_test = X.iloc[split_index:]

y_train = y.iloc[:split_index]
y_test = y.iloc[split_index:]

print("\nData split completed successfully!")

print("Training samples:", len(X_train))
print("Testing samples:", len(X_test))

print("X_train shape:", X_train.shape)
print("X_test shape:", X_test.shape)
print("y_train shape:", y_train.shape)
print("y_test shape:", y_test.shape)
from sklearn.linear_model import LinearRegression

# Create the Linear Regression model
model = LinearRegression()

# Train the model using training data
model.fit(X_train, y_train)

print("\nLinear Regression model trained successfully!")
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
import numpy as np

# Make predictions on the test data
y_pred = model.predict(X_test)

print("\nPredictions generated successfully!")

# Calculate evaluation metrics
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = np.sqrt(mse)
r2 = r2_score(y_test, y_pred)

print("\nLinear Regression Model Evaluation:")
print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R² Score:", r2)
from sklearn.ensemble import RandomForestRegressor

# Create the Random Forest model
rf_model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train the Random Forest model
rf_model.fit(X_train, y_train)

print("\nRandom Forest model trained successfully!")

# Make predictions on the test data
rf_pred = rf_model.predict(X_test)

# Evaluate the Random Forest model
rf_mae = mean_absolute_error(y_test, rf_pred)
rf_mse = mean_squared_error(y_test, rf_pred)
rf_rmse = np.sqrt(rf_mse)
rf_r2 = r2_score(y_test, rf_pred)

print("\nRandom Forest Model Evaluation:")
print("MAE:", rf_mae)
print("MSE:", rf_mse)
print("RMSE:", rf_rmse)
print("R² Score:", rf_r2)
import joblib

# Save the Linear Regression model
model_path = Path(__file__).parent / "weather_model.pkl"

joblib.dump(model, model_path)

print("\nLinear Regression model saved successfully!")
print("Model saved to:", model_path)
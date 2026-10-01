# AtmoSync

## Micro-Climate Arbitrage Analytics

AtmoSync is a data-driven weather analytics project that collects weather data, analyzes localized weather conditions, performs micro-climate comparisons, and predicts next-hour temperature using machine learning.

The project combines **Python, Pandas, Scikit-learn, FastAPI, and Streamlit** to create an end-to-end weather analytics and prediction system.

---

## Objectives

* Collect hourly weather data using the Open-Meteo API.
* Perform exploratory data analysis on weather conditions.
* Preprocess and organize weather data.
* Create useful time-based and weather-change features.
* Build a machine learning model for next-hour temperature prediction.
* Compare weather conditions across multiple locations around Hyderabad.
* Generate micro-climate indicators and insights.
* Provide a FastAPI backend for prediction and micro-climate data.
* Develop an interactive Streamlit dashboard.

---

##  Features

### Weather Data Collection

Weather data is collected using the **Open-Meteo API**.

The collected variables include:

* Temperature
* Relative humidity
* Precipitation
* Wind speed

The data is stored as CSV files for further processing.

### Exploratory Data Analysis

The project performs exploratory analysis using:

* Temperature trends
* Humidity trends
* Precipitation trends
* Wind-speed trends
* Correlation analysis
* Statistical summaries

### Data Preprocessing

The preprocessing stage includes:

* Missing-value checking
* Duplicate checking
* Date-time conversion
* Chronological sorting
* Dataset preparation

### Feature Engineering

The following features are created:

* Hour
* Day
* Month
* Day of week
* Temperature change
* Humidity change
* Wind-speed change

###  Machine Learning

A machine learning pipeline is used to predict the **next-hour temperature**.

Models evaluated:

* Linear Regression
* Random Forest Regression

For the current prototype dataset, Linear Regression produced lower test-set errors and was selected for integration with the API.

### Micro-Climate Analysis

Weather data is compared across multiple Hyderabad-area locations:

* Hyderabad Central
* HITEC City
* Secunderabad
* Gachibowli

The analysis calculates:

* Average temperature
* Average humidity
* Average wind speed
* Temperature difference from overall average
* Humidity difference from overall average
* Wind-speed difference from overall average

###  FastAPI Backend

FastAPI provides API endpoints for:

* Health/status checking
* Next-hour temperature prediction
* Micro-climate data

###  Streamlit Dashboard

The Streamlit dashboard provides:

* Weather summary metrics
* Location selection
* Temperature comparison
* Humidity comparison
* Wind-speed comparison
* Next-hour temperature prediction
* Micro-climate insights

---

##  System Architecture

```text
                    Open-Meteo API
                         │
                         ▼
                Weather Data Collection
                         │
                         ▼
                  Raw Weather Data
                         │
                         ▼
                Data Preprocessing
                         │
                         ▼
                 Feature Engineering
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Micro-Climate Analysis    ML Training
              │                     │
              ▼                     ▼
       Micro-Climate Data      Weather Model
              │                     │
              └──────────┬──────────┘
                         ▼
                   FastAPI Backend
                         │
                         ▼
                  Streamlit Dashboard
                         │
              ┌──────────┴──────────┐
              ▼                     ▼
       Climate Insights       Temperature
                              Prediction
```

---

## Technologies Used

| Technology       | Purpose                                   |
| ---------------- | ----------------------------------------- |
| Python           | Core programming language                 |
| Pandas           | Data processing and analysis              |
| NumPy            | Numerical operations                      |
| Matplotlib       | Data visualization                        |
| Seaborn          | Correlation and statistical visualization |
| Scikit-learn     | Machine learning                          |
| Joblib           | Model saving and loading                  |
| Requests         | API communication                         |
| Open-Meteo API   | Weather data source                       |
| FastAPI          | Backend API                               |
| Uvicorn          | FastAPI server                            |
| Streamlit        | Interactive dashboard                     |
| Plotly           | Interactive charts                        |
| Jupyter Notebook | Exploratory data analysis                 |
| Git & GitHub     | Version control                           |

---

## Project Structure

```text
AtmoSync/
│
├── data/
│   ├── .gitkeep
│   ├── fetch_weather.py
│   ├── preprocess_weather.py
│   ├── feature_engineering.py
│   ├── multi_location_weather.py
│   ├── microclimate_analysis.py
│   ├── microclimate_indicators.py
│   ├── microclimate_visualization.py
│   ├── microclimate_insights.py
│   ├── weather_data.csv
│   ├── processed_weather_data.csv
│   ├── feature_engineered_weather.csv
│   ├── multi_location_weather.csv
│   ├── microclimate_indicators.csv
│   └── microclimate_insights.txt
│
├── ml/
│   ├── train_model.py
│   └── weather_model.pkl
│
├── backend/
│   └── main.py
│
├── frontend/
│   └── app.py
│
├── notebooks/
│   └── weather_eda.ipynb
│
├── README.md
├── requirements.txt
├── .gitignore
└── LICENSE
```

---

## Dataset and Weather Data Source

AtmoSync uses weather data obtained through the **Open-Meteo API**.

The project collects hourly weather variables such as:

* Temperature at 2 metres
* Relative humidity
* Precipitation
* Wind speed at 10 metres

The current prototype uses weather forecast data for Hyderabad-area locations.

The multi-location dataset is used for comparative analysis and prototype development. It should not be interpreted as a validated measurement of real-world micro-climate differences.

---

## Machine Learning Model

The machine learning task is:

> **Predict the temperature for the next hour using current and derived weather features.**

### Input Features

* Current temperature
* Relative humidity
* Precipitation
* Wind speed
* Hour
* Day
* Month
* Day of week
* Temperature change
* Humidity change
* Wind-speed change

### Target

```text
Next-hour temperature
```

### Models Evaluated

**Linear Regression**

Test-set metrics:

* MAE: 0.156 °C
* MSE: 0.035
* RMSE: 0.187 °C
* R²: 0.996

**Random Forest Regression**

Test-set metrics:

* MAE: 0.310 °C
* MSE: 0.162
* RMSE: 0.403 °C
* R²: 0.981

These results are specific to the current prototype dataset and test split. They should not be treated as real-world forecasting performance.

---

## API Endpoints

The FastAPI backend provides the following endpoints.

### GET `/`

Checks whether the backend is running.

Example response:

```json
{
  "message": "Welcome to AtmoSync API",
  "status": "Backend is running"
}
```

### POST `/predict`

Predicts the next-hour temperature using weather input features.

### GET `/microclimate`

Returns micro-climate indicators for the analyzed locations.

---

##  Installation

Clone the repository:

```bash
git clone https://github.com/kandularakshitha24/AtmoSync.git
```

Move into the project directory:

```bash
cd AtmoSync
```

Install the required Python packages:

```bash
pip install -r requirements.txt
```

---

## How to Run

### 1. Collect Weather Data

Run:

```bash
python data\fetch_weather.py
```

### 2. Preprocess the Data

Run:

```bash
python data\preprocess_weather.py
```

### 3. Perform Feature Engineering

Run:

```bash
python data\feature_engineering.py
```

### 4. Train the ML Model

Run:

```bash
python ml\train_model.py
```

### 5. Start FastAPI

Open a terminal and run:

```bash
uvicorn backend.main:app --reload
```

FastAPI will run at:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 6. Start Streamlit

Open another terminal and run:

```bash
streamlit run frontend\app.py
```

The dashboard will be available at:

```text
http://localhost:8501
```

---

## Current Prototype Results

The current prototype successfully demonstrates:

* Hourly weather data collection
* Weather data preprocessing
* Feature engineering
* Machine learning-based temperature prediction
* Multi-location weather comparison
* Micro-climate indicator generation
* FastAPI backend integration
* Interactive Streamlit dashboard

Example prediction from the integrated system:

```text
Predicted Next-Hour Temperature: 30.41 °C
```

---

## Limitations

* The current prototype uses a relatively small weather dataset.
* The collected Open-Meteo data is forecast data rather than a long-term historical observation dataset.
* The current multi-location comparison is intended for prototype analysis and does not establish validated real-world micro-climate differences.
* Larger historical datasets would be required for stronger machine learning validation.
* Additional environmental variables could improve future predictions.
* The current model focuses only on next-hour temperature prediction.

---

##  Future Scope

Future versions of AtmoSync can include:

* Long-term historical weather datasets
* More Hyderabad locations
* Real-time weather monitoring
* Additional weather and environmental variables
* More advanced machine learning models
* Deep learning-based forecasting
* Time-series forecasting models
* Interactive geographical weather maps
* Anomaly detection
* Automated weather alerts
* Cloud deployment
* More advanced micro-climate analytics

---

## Project Status

**Status: Prototype Completed**

The current version demonstrates an end-to-end pipeline from weather data collection to machine learning prediction and interactive dashboard visualization.

---

## Author

**Kandula Rakshitha**

B.Tech - Computer Science and Machine Learning

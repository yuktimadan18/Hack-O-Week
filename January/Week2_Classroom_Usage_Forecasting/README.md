# Week 2 – Classroom Electricity Usage Forecast

## Problem Statement
Classrooms consume electricity for lighting, projectors, and air conditioning. Predicting electricity demand can help institutions manage power supply efficiently.

This project forecasts **future classroom electricity usage using time-series forecasting techniques**.

---

## Objectives
- Analyze classroom electricity consumption patterns
- Apply time-series forecasting
- Predict future electricity demand
- Visualize predicted energy trends

---

## Dataset
A synthetic dataset representing classroom electricity consumption was generated.

Features:

- `timestamp` – Time of electricity measurement
- `electricity_usage_kwh` – Energy consumption
- `predicted_usage` – Forecasted electricity demand

---

## Methodology

### 1. Time-Series Analysis
Electricity usage data was treated as a time-series dataset.

### 2. ARIMA Model
The **ARIMA (AutoRegressive Integrated Moving Average)** model was used to forecast future electricity demand.

### 3. Forecast Generation
Future electricity usage was predicted based on historical trends.

### 4. Visualization
Graphs were created to compare actual electricity usage and predicted values.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- Streamlit

---

## Project Structure
Week2_Classroom_Forecast
│
├── data
├── notebooks
│ └── classroom_energy_forecast.ipynb
├── dashboard
│ └── app.py
└── src


---

## Dashboard

Run the dashboard using:


streamlit run app.py

The dashboard displays:

- Classroom electricity usage trends
- Forecasted electricity demand
- Confidence intervals

---

## Outcome
The forecasting system helps optimize electricity distribution across classrooms and assists administrators in planning energy usage efficiently.
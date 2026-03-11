# Week 3 – Library Energy Usage During Exams

## Problem Statement
Library usage increases significantly during exam periods, resulting in higher electricity consumption.

The objective of this project is to **predict library electricity demand during exam periods using time-series forecasting**.

---

## Objectives
- Analyze library electricity usage patterns
- Simulate exam-period energy surge
- Forecast future electricity demand
- Visualize predicted energy trends

---

## Dataset
A synthetic dataset representing daily library electricity usage was generated.

Features:

- `date` – Date of electricity measurement
- `energy_usage_kwh` – Electricity consumption
- `predicted_usage` – Forecasted electricity usage

The dataset also simulates increased energy consumption during exam periods.

---

## Methodology

### 1. Data Generation
Daily electricity usage data was generated for 120 days.

### 2. Exam Period Simulation
The last 20 days simulate increased electricity consumption during exam periods.

### 3. Exponential Smoothing Model
The **Exponential Smoothing forecasting model** was applied to predict short-term electricity demand.

### 4. Forecasting
The model predicts electricity usage for the next 14 days.

### 5. Visualization
Graphs were created to compare actual electricity usage with predicted demand.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Statsmodels
- Matplotlib
- Plotly
- Streamlit

---

## Project Structure
Week3_Library_Energy_Exams
│
├── data
│ ├── library_energy_usage.csv
│ └── library_energy_forecast.csv
│
├── notebooks
│ └── library_energy_forecast.ipynb
│
├── dashboard
│ └── app.py
│
└── src


---

## Dashboard

Run the dashboard using:


streamlit run app.py

The dashboard displays:

- Current library energy usage
- Predicted exam-period energy demand
- Gauge-style energy monitoring visualization

---

## Outcome
This system helps predict energy demand during exam periods and supports efficient energy management in campus libraries.



# Week 1 – Dorm Electricity Spike Detection

## Problem Statement
Campus dormitories consume electricity continuously throughout the day. Sudden spikes in electricity usage may indicate abnormal appliance usage, electrical faults, or inefficient energy consumption.

The goal of this project is to **detect unusual spikes in dorm electricity usage using data analysis techniques**.

---

## Objectives
- Analyze hourly dorm electricity usage
- Detect abnormal spikes in energy consumption
- Visualize energy usage trends
- Build a monitoring dashboard

---

## Dataset
A synthetic dataset was generated to simulate hourly dorm electricity consumption.

Features:

- `timestamp` – Date and time of electricity measurement
- `electricity_usage_kwh` – Electricity usage in kilowatt-hours
- `moving_avg` – Moving average of electricity usage
- `spike` – Flag indicating abnormal electricity spike

---

## Methodology

### 1. Data Generation
Synthetic electricity usage data was generated to simulate dormitory consumption patterns.

### 2. Moving Average Calculation
A moving average was computed to identify normal electricity usage patterns.

### 3. Spike Detection
Spikes were detected when electricity usage exceeded a predefined threshold above the moving average.

### 4. Visualization
Time-series plots were created to visualize electricity usage and spike occurrences.

---

## Technologies Used
- Python
- Pandas
- NumPy
- Matplotlib
- Streamlit

---

## Project Structure
Week1_Electricity_Spikes
│
├── data
├── notebooks
│ └── electricity_spike_detection.ipynb
├── dashboard
│ └── app.py
└── src


---

## Dashboard

Run the dashboard using:

streamlit run app.py


The dashboard displays:

- Electricity usage trends
- Detected spikes
- Monitoring visualization

---

## Outcome
This system helps identify abnormal electricity consumption patterns in dormitories and improves energy monitoring across campus housing.
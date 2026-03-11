import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Classroom Electricity Usage Forecast 📊")

# Load datasets
usage_data = pd.read_csv("../data/classroom_usage.csv")
forecast_data = pd.read_csv("../data/classroom_forecast.csv")

# Convert timestamps
usage_data["timestamp"] = pd.to_datetime(usage_data["timestamp"])
forecast_data["timestamp"] = pd.to_datetime(forecast_data["timestamp"])

# Create chart
fig = go.Figure()

# Actual electricity usage
fig.add_trace(go.Scatter(
    x=usage_data["timestamp"],
    y=usage_data["electricity_usage_kwh"],
    mode="lines",
    name="Actual Usage"
))

# Forecast line
fig.add_trace(go.Scatter(
    x=forecast_data["timestamp"],
    y=forecast_data["predicted_usage"],
    mode="lines",
    name="Forecast"
))

# Confidence interval
fig.add_trace(go.Scatter(
    x=forecast_data["timestamp"],
    y=forecast_data["upper_bound"],
    mode="lines",
    line=dict(width=0),
    showlegend=False
))

fig.add_trace(go.Scatter(
    x=forecast_data["timestamp"],
    y=forecast_data["lower_bound"],
    mode="lines",
    fill='tonexty',
    name="Confidence Interval"
))

st.plotly_chart(fig)

st.subheader("Forecast Data")
st.dataframe(forecast_data)
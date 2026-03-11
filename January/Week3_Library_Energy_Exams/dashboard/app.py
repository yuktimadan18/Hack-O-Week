import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("📚 Library Energy Monitor")

# Load data
usage_data = pd.read_csv("../data/library_energy_usage.csv")
forecast_data = pd.read_csv("../data/library_energy_forecast.csv")

# Convert date columns
usage_data["date"] = pd.to_datetime(usage_data["date"])
forecast_data["date"] = pd.to_datetime(forecast_data["date"])

# Current usage
current_usage = usage_data["energy_usage_kwh"].iloc[-1]

# Predicted peak usage
predicted_peak = forecast_data["predicted_usage"].max()

st.write("### Current Energy Usage:", round(current_usage,2), "kWh")
st.write("### Predicted Exam Peak:", round(predicted_peak,2), "kWh")

# Gauge chart
fig = go.Figure(go.Indicator(
    mode="gauge+number",
    value=current_usage,
    title={"text": "Library Energy Load"},
    gauge={
        "axis": {"range": [0, predicted_peak*1.2]},
        "bar": {"color": "orange"},
        "steps": [
            {"range": [0, predicted_peak*0.5], "color": "lightgreen"},
            {"range": [predicted_peak*0.5, predicted_peak], "color": "yellow"},
            {"range": [predicted_peak, predicted_peak*1.2], "color": "red"},
        ],
    }
))

st.plotly_chart(fig)

st.subheader("Forecast Data")
st.dataframe(forecast_data)
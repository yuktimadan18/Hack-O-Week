import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("Dorm Electricity Usage Dashboard")

# Load data
data = pd.read_csv("../data/electricity_processed.csv")
data["timestamp"] = pd.to_datetime(data["timestamp"])

# Sidebar filters
st.sidebar.header("Filters")

# Date filter
start_date = st.sidebar.date_input("Start Date", data["timestamp"].min().date())
end_date = st.sidebar.date_input("End Date", data["timestamp"].max().date())

# Hour filter
hour_range = st.sidebar.slider("Hour Range", 0, 23, (0, 23))

# Apply filters
filtered_data = data[
    (data["timestamp"].dt.date >= start_date) &
    (data["timestamp"].dt.date <= end_date) &
    (data["hour"] >= hour_range[0]) &
    (data["hour"] <= hour_range[1])
]

# KPI calculations
avg_usage = data["electricity_usage_kwh"].mean()
max_usage = data["electricity_usage_kwh"].max()
total_spikes = data["spike"].sum()

# Display KPIs
col1, col2, col3 = st.columns(3)

col1.metric("Average Usage (kWh)", round(avg_usage, 2))
col2.metric("Max Usage (kWh)", round(max_usage, 2))
col3.metric("Total Spikes Detected", int(total_spikes))



# Create figure
fig = go.Figure()

# Actual usage
fig.add_trace(go.Scatter(
    x=filtered_data["timestamp"],
    y=filtered_data["electricity_usage_kwh"],
    mode="lines",
    name="Actual Usage"
))

# Moving average
fig.add_trace(go.Scatter(
    x=filtered_data["timestamp"],
    y=filtered_data["moving_avg"],
    mode="lines",
    name="Moving Average"
))

# Spike markers
spikes = filtered_data[filtered_data["spike"] == True]

fig.add_trace(go.Scatter(
    x=spikes["timestamp"],
    y=spikes["electricity_usage_kwh"],
    mode="markers",
    name="Spike",
    marker=dict(size=10)
))

st.plotly_chart(fig)

st.subheader("Detected Electricity Spikes")
st.dataframe(spikes)
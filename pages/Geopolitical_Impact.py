import streamlit as st
import pandas as pd
import plotly.graph_objects as go

st.title("⚠️ Geopolitical Impact Analysis")

# Load data
market = pd.read_csv(
    "data/final_data/combined_data.csv"
)

events = pd.read_csv(
    "data/final_data/data_encoded.csv"
)

# Convert dates
market["Date"] = pd.to_datetime(market["Date"])
events["Date"] = pd.to_datetime(events["Date"])

# Create chart
fig = go.Figure()

# Oil line
fig.add_trace(
    go.Scatter(
        x=market["Date"],
        y=market["Oil"],
        mode="lines",
        name="Oil"
    )
)

# NASDAQ line
fig.add_trace(
    go.Scatter(
        x=market["Date"],
        y=market["NASDAQ"],
        mode="lines",
        name="NASDAQ"
    )
)

# Add geopolitical event markers
for _, row in events.iterrows():

    event_date = row["Date"].strftime("%Y-%m-%d")

    fig.add_vline(
        x=event_date,
        line_dash="dash",
        line_color="red"
    )

# Layout
fig.update_layout(
    template="plotly_dark",
    height=700,
    title="Market Changes During Geopolitical Events",
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

st.subheader("Major Events")

st.dataframe(
    events,
    use_container_width=True
)

st.info(
"""
COVID-19:
• Global lockdowns reduced demand
• Oil prices dropped sharply

Russia–Saudi Oil War:
• Oil market volatility increased

Inflation Period:
• Currency and stock markets reacted strongly
"""
)
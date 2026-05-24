import streamlit as st
import pandas as pd
import plotly.express as px

st.title("🌍 Market Relationship Analysis")

# Load data
df = pd.read_csv(
    "data/final_data/combined_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# --------------------------------
# CHART 1
# Normalized comparison
# --------------------------------

st.subheader("Normalized Market Comparison")

fig = px.line(
    df,
    x="Date",
    y=[
        "Oil",
        "SP500",
        "NASDAQ",
        "USD_Normalized"
    ]
)

fig.update_layout(
    template="plotly_dark",
    height=600,
    hovermode="x unified"
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# --------------------------------
# CHART 2
# USD vs Oil
# --------------------------------

st.subheader("USD vs Oil Relationship")

fig2 = px.scatter(
    df,
    x="USD_Return",
    y="Oil"
)

fig2.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig2,
    use_container_width=True
)

# --------------------------------
# CHART 3
# USD vs NASDAQ
# --------------------------------

st.subheader("USD vs NASDAQ Relationship")

fig3 = px.scatter(
    df,
    x="USD_Return",
    y="NASDAQ"
)

fig3.update_layout(
    template="plotly_dark"
)

st.plotly_chart(
    fig3,
    use_container_width=True
)
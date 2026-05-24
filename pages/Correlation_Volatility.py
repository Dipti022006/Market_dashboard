import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📊 Correlation & Volatility")

df = pd.read_csv(
    "data/final_data/combined_data.csv"
)

df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# Correlation heatmap
# -----------------------------

corr = df[
[
"Oil",
"SP500",
"NASDAQ",
"USD_Index"
]
].corr()

fig = px.imshow(
    corr,
    text_auto=True
)

fig.update_layout(
    template="plotly_dark",
    height=600
)

st.plotly_chart(
    fig,
    use_container_width=True
)

# -----------------------------
# Volatility
# -----------------------------

df["Oil_Volatility"] = (
    df["Oil"]
    .rolling(20)
    .std()
)

fig2 = px.line(
    df,
    x="Date",
    y="Oil_Volatility"
)

fig2.update_layout(
    template="plotly_dark",
    height=500
)

st.plotly_chart(
    fig2,
    use_container_width=True
)
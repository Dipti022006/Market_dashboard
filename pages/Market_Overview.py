import streamlit as st
import pandas as pd
import plotly.express as px

st.title("📈 Market Overview")

df = pd.read_csv(
"data/final_data/combined_data.csv"
)

df["Date"]=pd.to_datetime(df["Date"])

year=st.sidebar.selectbox(
"Year",
sorted(df["Date"].dt.year.unique())
)

filtered=df[
df["Date"].dt.year==year
]

c1,c2,c3,c4=st.columns(4)

c1.metric(
"🛢 Oil",
round(filtered["Oil"].iloc[-1],2)
)

c2.metric(
"📊 SP500",
round(filtered["SP500"].iloc[-1],2)
)

c3.metric(
"📈 NASDAQ",
round(filtered["NASDAQ"].iloc[-1],2)
)

c4.metric(
"💵 USD",
round(filtered["USD_Index"].iloc[-1],2)
)

fig=px.line(
filtered,
x="Date",
y=[
"Oil",
"SP500",
"NASDAQ",
"USD_Normalized"
],
title="Global Market Trends"
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
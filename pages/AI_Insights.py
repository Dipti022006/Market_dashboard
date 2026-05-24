import streamlit as st
import pandas as pd

st.title("🤖 AI Market Insights")

df = pd.read_csv("data/final_data/combined_data.csv")
df["Date"] = pd.to_datetime(df["Date"])

# -----------------------------
# BASIC STATS
# -----------------------------

oil_change = df["Oil"].iloc[-1] - df["Oil"].iloc[0]
nasdaq_change = df["NASDAQ"].iloc[-1] - df["NASDAQ"].iloc[0]
sp500_change = df["SP500"].iloc[-1] - df["SP500"].iloc[0]

usd_change = df["USD_Index"].iloc[-1] - df["USD_Index"].iloc[0]

st.subheader("📊 Overall Market Movement")

st.write(f"🛢 Oil Change: {oil_change:.2f}")
st.write(f"📈 NASDAQ Change: {nasdaq_change:.2f}")
st.write(f"📊 SP500 Change: {sp500_change:.2f}")
st.write(f"💵 USD Change: {usd_change:.2f}")
performance = {
    "Oil": oil_change,
    "NASDAQ": nasdaq_change,
    "SP500": sp500_change,
    "USD": usd_change
}

best = max(performance, key=performance.get)
worst = min(performance, key=performance.get)

st.subheader("🏆 Performance Summary")

st.success(f"Best Performing Asset: {best}")
st.error(f"Worst Performing Asset: {worst}")
df["Oil_vol"] = df["Oil"].rolling(20).std()
df["NASDAQ_vol"] = df["NASDAQ"].rolling(20).std()

most_volatile = (
    "Oil"
    if df["Oil_vol"].mean() > df["NASDAQ_vol"].mean()
    else "NASDAQ"
)

st.subheader("⚡ Volatility Insight")

st.warning(f"Most Volatile Market: {most_volatile}")
st.subheader("🧠 AI Interpretation")

st.info("""
• Oil reacts strongly to geopolitical events like wars and supply shocks  
• NASDAQ is sensitive to inflation and interest rate changes  
• USD strengthens during global uncertainty  
• Markets show synchronized drops during COVID period  
""")
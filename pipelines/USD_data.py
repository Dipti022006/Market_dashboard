import yfinance as yf
import pandas as pd

# -----------------------------
# STEP 1: DOWNLOAD USD DATA
# -----------------------------
# US Dollar Index (DXY futures)
ticker = "DX-Y.NYB"

df = yf.download(ticker, start="2020-01-01", end="2026-01-01")

# -----------------------------
# STEP 2: CLEAN DATA
# -----------------------------
df = df[["Close"]].reset_index()
df.columns = ["Date", "USD_Index"]

# Ensure numeric
df["USD_Index"] = df["USD_Index"].astype(float)

# -----------------------------
# STEP 3: NORMALIZATION (BASE = 100)
# -----------------------------
df["USD_Normalized"] = (df["USD_Index"] / df["USD_Index"].iloc[0]) * 100

# -----------------------------
# STEP 4: DAILY RETURN (OPTIONAL BUT POWERFUL)
# -----------------------------
df["USD_Return"] = df["USD_Index"].pct_change() * 100

# -----------------------------
# STEP 5: SAVE FILE
# -----------------------------
df.to_csv("data/final_data/USD.csv", index=False)

print("USD dataset created + normalized successfully!")
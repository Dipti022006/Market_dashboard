import os
import pandas as pd

# Load raw dataset
df = pd.read_csv("data/raw/market_data.csv")  # (use your market file if different)

# Ensure correct date format
df["Date"] = pd.to_datetime(df["Date"])

# Sort by date (VERY IMPORTANT for indexing)
df = df.sort_values("Date")

# -------------------------------
# 📊 NORMALIZATION (BASE = 100)
# -------------------------------

df["Oil"] = (df["Oil"] / df["Oil"].iloc[0]) * 100
df["SP500"] = (df["SP500"] / df["SP500"].iloc[0]) * 100
df["NASDAQ"] = (df["NASDAQ"] / df["NASDAQ"].iloc[0]) * 100

# -------------------------------
# OPTIONAL: KEEP ORIGINAL DATA TOO
# -------------------------------
# (Good practice for analysis)
# df["Oil_raw"] = df["Oil"]

# -------------------------------
# CREATE OUTPUT FOLDER
# -------------------------------
os.makedirs("data/raw", exist_ok=True)

# Save processed file
df.to_csv("data/final_data/cleaned_market_data.csv", index=False)

print("Normalized market dataset created successfully!")
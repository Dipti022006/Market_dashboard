import pandas as pd

# Load market data
market = pd.read_csv("data/final_data/cleaned_market_data.csv")

# Load USD data
usd = pd.read_csv("data/final_data/USD.csv")

# Convert Date to same format
market["Date"] = pd.to_datetime(market["Date"])
usd["Date"] = pd.to_datetime(usd["Date"])

# Merge on Date
df = pd.merge(market, usd, on="Date", how="inner")

# Save final dataset
df.to_csv("data/final_data/combined_data.csv", index=False)

print("Merge completed successfully")
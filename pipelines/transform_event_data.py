import pandas as pd

# Load raw events dataset
df = pd.read_csv("data/raw/geopolitical_events.csv")

# Convert Impact_Level → numeric
impact_map = {
    "Low": 1,
    "Medium": 2,
    "High": 3,
    "Very High": 4,
    "Extreme": 5
}

df["Impact_Score"] = df["Impact_Level"].map(impact_map)

# Optional: ensure date format
df["Date"] = pd.to_datetime(df["Date"])

# Save processed dataset
df.to_csv("data/final_data/data_encoded.csv", index=False)

print("Events transformation completed successfully!")
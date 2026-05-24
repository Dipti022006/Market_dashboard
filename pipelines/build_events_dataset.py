import pandas as pd

events = [

# =========================
# 🌍 2020 - COVID & SHOCKS
# =========================
("2020-01-30", "WHO Declares COVID-19 Global Emergency", "Global Health Crisis", "High"),
("2020-03-11", "COVID-19 Declared Pandemic", "Global Health Crisis", "Very High"),
("2020-04-20", "Oil Prices Turn Negative (WTI Crash)", "Oil Shock", "Extreme"),
("2020-03-08", "Russia–Saudi Arabia Oil Price War", "Oil Shock", "High"),
("2020-03-27", "Global Lockdowns Expand Worldwide", "Economic Crisis", "Very High"),

# =========================
# 🌍 2021 - Recovery + Supply Chains
# =========================
("2021-03-23", "Ever Given Blocks Suez Canal", "Trade Disruption", "High"),
("2021-08-15", "Afghanistan Government Collapse", "Geopolitical Conflict", "Medium"),
("2021-10-01", "Global Energy Crisis Begins", "Energy Crisis", "High"),

# =========================
# 🌍 2022 - WAR ERA SHOCK
# =========================
("2022-02-24", "Russia Invades Ukraine", "War", "Extreme"),
("2022-03-01", "Oil Prices Cross $100", "Oil Shock", "Very High"),
("2022-03-06", "Global Sanctions on Russia Expand", "Economic Sanctions", "High"),
("2022-10-05", "OPEC+ Cuts Oil Production", "Oil Supply Policy", "High"),

# =========================
# 🌍 2023 - TENSIONS + ENERGY
# =========================
("2023-10-07", "Israel–Hamas War Begins", "Geopolitical Conflict", "High"),
("2023-01-15", "Global Inflation Peak Phase", "Economic Crisis", "High"),

# =========================
# 🌍 2024 - SHIPPING + REGIONAL CONFLICTS
# =========================
("2024-01-12", "Red Sea Shipping Attacks Begin", "Trade Disruption", "High"),
("2024-06-01", "OPEC Maintains Production Cuts", "Oil Supply Policy", "Medium"),

# =========================
# 🌍 2025 - MARKET VOLATILITY
# =========================
("2025-03-01", "Global Oil Oversupply Concerns", "Oil Market", "Medium"),
("2025-09-15", "China Economic Slowdown Impacts Oil Demand", "Economic Crisis", "High"),

# =========================
# 🌍 2026 - MODERN ENERGY WARFARE ERA
# =========================
("2026-02-01", "Iran Conflict Escalation Impacts Strait of Hormuz", "War", "Extreme"),
("2026-04-29", "Drone Attacks on Russian Oil Infrastructure", "War", "High"),
("2026-05-10", "OPEC Output Drops Due to Global Tensions", "Oil Supply Policy", "High"),

]

df = pd.DataFrame(events, columns=["Date", "Event", "Category", "Impact_Level"])

df["Date"] = pd.to_datetime(df["Date"])

df.to_csv("data/raw/geopolitical_events.csv", index=False)

print("Professional geopolitical dataset created!")
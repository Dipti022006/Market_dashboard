import streamlit as st

st.set_page_config(
    page_title="Global Market Intelligence Dashboard",
    page_icon="🌍",
    layout="wide"
)

st.title("🌍 Global Market Intelligence Dashboard")

st.markdown("""
### Understand how global events reshape financial markets

Features:

✔ Market Overview  
✔ USD–Oil relationship analysis  
✔ Geopolitical impact visualization  
✔ Volatility analysis  
✔ AI insights and forecasting
""")

st.image(
"https://images.unsplash.com/photo-1611974789855-9c2a0a7236a3",
use_container_width=True
)

st.info(
"Select a page from the sidebar to begin analysis."
)
import streamlit as st

# Define your pages and clean URL paths
home_page = st.Page("home.py", title="Home", icon="🏠", default=True)
persity_page = st.Page(
    "persity_app.py",
    title="Personality & Behavior",
    icon="🧠",
    url_path="persity",
)
authorship_page = st.Page(
    "authorship_app.py",
    title="Books & Authorship",
    icon="📚",
    url_path="authorship",
)

# Set up navigation configuration
pg = st.navigation([home_page, persity_page, authorship_page])

st.set_page_config(
    page_title="Piravi Ecosystem", page_icon="✨", layout="wide"
)

pg.run()

import streamlit as st
import numpy as np
import pandas as pd
import geopy

from geopy.geocoders import Nominatim
from geopy.extra.rate_limiter import RateLimiter

st.header("Best Work-Life Balance Cities in 2022")

df = pd.read_csv("https://raw.githubusercontent.com/NhudaAziz/FinalChallenge/main/Cities%20with%20the%20Best%20Work-Life%20Balance%202022.csv")

# ---- Sidebar ----
st.sidebar.header("Choose Filter:")
country = st.sidebar.multiselect(
    "Select the Country:",
    options=df["Country"].unique(),
    default=df["Country"].unique()
)

city = st.sidebar.multiselect(
    "Select the City:",
    options=df["City"].unique(),
    default=df["City"].unique()
)

df_selection = df.query(
    "Country == @country & City == @city"
)

geolocator = Nominatim(user_agent="GTA Lookup")
geocode = RateLimiter(geolocator.geocode, min_delay_seconds=1)
location = geolocator.geocode(country+", "+city)

lat = location.latitude
lon = location.longitude

map_data = pd.DataFrame({'lat': [lat], 'lon': [lon]})

st.map(map_data)

#st.line_chart(chart_data)

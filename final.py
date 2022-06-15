import streamlit as st
import numpy as np
import pandas as pd
import plotly.express as px

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

# BAR CHART
city_remote_line = (
    df_selection.groupby(by=["City"]).sum()[["Remote Jobs"]].sort_values(by="Remote Jobs")
    
fig_city = px.bar(
    city_remote_line,
    x="Remote Jobs",
    y=city_remote_line.index,
    orientation="h",
    title="<b>Remote Jobs in Cities</b>",
    color_discrete_sequence=["#0083B8"] * len(city_remote_line),
    template="plotly_white",
)
fig_city.update_layout(
    plot_bgcolor="rgba(0,0,0,0)",
    xaxis=(dict(showgrid=False))
)

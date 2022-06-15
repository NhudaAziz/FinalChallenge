import streamlit as st
import numpy as np
import pandas as pd

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

chart_data = pd.DataFrame(
     np.random.randn(20, 3), #20 rows 3 columns
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

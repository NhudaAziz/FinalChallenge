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
city_line = (
    df_selection.groupby(by=('Country')['City'].count().sort_values(ascending=True).plot.barh(figsize=(10,8))
)
# fig_product_sales = px.bar(
#     sales_by_product_line,
#     x="Total",
#     y=sales_by_product_line.index,
#     orientation="h",
#     title="<b>Sales by Product Line</b>",
#     color_discrete_sequence=["#0083B8"] * len(sales_by_product_line),
#     template="plotly_white",
# )
# fig_product_sales.update_layout(
#     plot_bgcolor="rgba(0,0,0,0)",
#     xaxis=(dict(showgrid=False))
# )

import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# from sklearn.ensemble import RandomForestClassifier

st.header("My first Streamlit App")
st.title("This is a title")

st.write("""
# This is a first-level heading
## This is a second-level heading
""")

st.write(pd.DataFrame({
    'Intplan': ['yes', 'yes', 'yes', 'no'],
    'Churn Status': [0, 0, 0, 1]
}))

# st.write("""
# # Disney Movies Gross Income
# This is the total gross income for the Disney movies from 1937 - 2016
# """)

# gross = pd.read_csv("https://raw.githubusercontent.com/NhudaAziz/FinalChallenge/main/disney_movies_total_gross.csv")
# feature_cols = ['movie_title','release_date','genre','mpaa_rating']
# # X = gross[feature_cols]
# Y = gross.inflation_adjusted_gross

# chart_data = pd.DataFrame(
#      np.random.randn(20, 3), #20 rows 3 columns
#      columns=['a', 'b', 'c'])

# st.line_chart(chart_data)


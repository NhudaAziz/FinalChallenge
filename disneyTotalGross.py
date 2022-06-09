import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Disney Movies Gross Income

""")

gross = pd.read_csv("https://raw.githubusercontent.com/NhudaAziz/FinalChallenge/main/disney_movies_total_gross.csv")
feature_cols = ['movie_title','release_date','genre','mpaa_rating']
X = gross[feature_cols]
Y = gross.inflation_adjusted_gross

chart_data = pd.DataFrame(
     np.random.randn(20, 3), #20 rows 3 columns
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)


import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.ensemble import RandomForestClassifier

st.write("""
# Disney Movies Gross Income

""")

st.sidebar.header('User Input Parameters')

def user_input_features():
    sepal_length = st.sidebar.slider('Sepal length', 4.3, 7.9, 5.4)
    sepal_width = st.sidebar.slider('Sepal width', 2.0, 4.4, 3.4)
    petal_length = st.sidebar.slider('Petal length', 1.0, 6.9, 1.3)
    petal_width = st.sidebar.slider('Petal width', 0.1, 2.5, 0.2)
    data = {'sepal_length': sepal_length,
            'sepal_width': sepal_width,
            'petal_length': petal_length,
            'petal_width': petal_width}
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

st.subheader('User Input parameters')
st.write(df)

gross = pd.read_csv("https://raw.githubusercontent.com/NhudaAziz/FinalChallenge/main/disney_movies_total_gross.csv")
feature_cols = ['movie_title','release_date','genre','mpaa_rating']
X = gross[feature_cols]
Y = gross.inflation_adjusted_gross

clf = RandomForestClassifier()
clf.fit(X, Y)

prediction = clf.predict(df)
prediction_proba = clf.predict_proba(df)

st.subheader('Class labels and their corresponding index number')
#y_label = ['setosa','versicolor','virginica']
st.write(pd.DataFrame({
     'Species': ['setosa','versicolor','virginica'],
 }))

st.subheader('Prediction')
#st.write(iris.target_names[prediction])
st.write(prediction)
st.image(
    "https://miro.medium.com/max/1000/1*nfK3vGZkTa4GrO7yWpcS-Q.png"
)

st.subheader('Prediction Probability')
st.write(prediction_proba)

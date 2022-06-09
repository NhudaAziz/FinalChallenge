import streamlit as st
import numpy as np
import pandas as pd
st.header("My first Streamlit App")

chart_data = pd.DataFrame(
     np.random.randn(20, 3), #20 rows 3 columns
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

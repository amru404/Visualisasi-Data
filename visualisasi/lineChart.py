import streamlit as st 
import pandas as pd
import numpy as np

st.title("Line Chart")
st.write("kelompok 23")
st.markdown("""
    1. Amru Abdurrahman Azzam - 0110122322
    2. Hayatunnisa - 0110222118
    3. Nurul Maedatul Awaliah 0110122222
""")

df = pd.DataFrame(
    np.random.randn(40,4),
    columns = ["c1","c2","c3","c4"]
)

#line chart
st.line_chart(df)
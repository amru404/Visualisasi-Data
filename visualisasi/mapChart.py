import streamlit as st 
import pandas as pd
import numpy as np

st.title("Map Chart")
st.write("kelompok 23")
st.markdown("""
    1. Amru Abdurrahman Azzam - 0110122322
    2. Hayatunnisa - 0110222118
    3. Nurul Maedatul Awaliah 0110122222
""")

df = pd.DataFrame(
    np.random.randn(50,2)/[10,10]+[15.3589,75.0078],
    columns=["latitude","longitude"]
)

st.map(df)
import streamlit as st

st.title("SideBar")
st.write("kelompok 23")
st.markdown("""
    1. Amru Abdurrahman Azzam - 0110122322
    2. Hayatunnisa - 0110222118
    3. Nurul Maedatul Awaliah 0110122222
""")

st.sidebar.title("Menu Chart")
st.sidebar.radio("Pilih chart", ["Bar Chart","Line Chart","Area Chart"])


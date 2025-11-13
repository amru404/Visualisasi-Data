import streamlit as st

st.title("Column")
st.write("kelompok 23")
st.markdown("""
    1. Amru Abdurrahman Azzam - 0110122322
    2. Hayatunnisa - 0110222118
    3. Nurul Maedatul Awaliah 0110122222
""")

col1, col2 = st.columns(2)

col1.write("ini adalah kolom pertama")
col1.image("https://d1bpj0tv6vfxyp.cloudfront.net/articles/538508_2-3-2021_10-55-48.webp", caption="kucink") #kalo mau pke local langsung arahin ke direktori aja, dibaca dri file ini -> lokasi aset   
col2.write("ini adalah kolom kedua")
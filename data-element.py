import streamlit as st
import pandas as pd #ngelola data dlm bntuk tabel
import numpy as np  #bkin data numb acak
import altair as alt #bkin chart interaktif

st.title("Praktikum 1 streamlit")
st.subheader("bagian data element")
st.markdown("""
1. Amru Abdurrahman Azzam - 0110122322
2. Hayatunnisa - 0110222118
3. Nurul Maedatul Awaliah 0110122222
""")

#DataFrame
st.subheader("DataFrame")
df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.dataframe(df)

st.subheader("highlight minimum value di dataframe")

st.dataframe(df.style.highlight_min(axis=0))

st.subheader("tabel statis")

df = pd.DataFrame(
    np.random.randn(30,10),
    columns=('col_no %d' % i for i in range (10))
)

st.table(df)

st.subheader("matric")
st.metric(label="temperatur", value="31 c", delta="1.2 c")

col1, col2, col3 = st.columns(3)    

col1.metric("Curah Hujan", "100 cm", "10 cm") # naik dan baik
col2.metric(label="Populasi", value="123 Miliar", delta="1 Miliar",delta_color="inverse")# naik tapi buruk 
col3.metric (label="Pelanggan", value=100, delta=10,delta_color="off") # netral (tidak baik, tidak buruk)
#Hanampilkan matrik tambahan dengan nilai kosong atau nol
st.metric(label="Speed", value=None, delta=0) #kosong naik baik karena di setting default
st.metric("Trees", "91456", "-1132649") #penurunan
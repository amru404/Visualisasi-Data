import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd

suhu = [20,22,24,26,28,30,32,35]
penjualan = [50,60,70,80,90,100,110,120]
penjualan_weekdays=[50,60,70,80,90,110,80,40]
penjualan_weekends=[100,110,120,130,100,200,230,40]

data = {
    'suhu' :  [20,22,24,26,28,30,32,35],
    'penjualan_Strawberi' :  [56,65,72,88,90,20,50,70],
    'penjualan_Cokelat' :  [60,20,90,80,50,40,60,20],
    'penjualan_Vanila' :  [20,60,70,80,90,100,110,120],
    'kelembapan': [20,23,25,19,25,20,23,26]
}

df = pd.DataFrame(data)

st.title('visualisasi scatter plot penjualan eskrim')
st.sidebar.header('pengaturan visualisasi')

option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
                             ("Basic Scatter Plot", 
                              "Kustomisasi Scatter Plot", 
                              "Multiple Scatter PLot",
                              "Analisis Scatter Plot"))
#identitas Kelompok
st.caption('Praktikum 5 - Matplotlib Scatter Plot')
st.markdown(""" 
Kelompok 23 :
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
            
""")

def basic_scatter():
    st.subheader('Basic Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan")
    st.pyplot(fig)

def Kustomisasi_scatter():
    st.subheader('Kustomisasi Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu, penjualan, color='orange',s=100,edgecolor="black",alpha=0.8)
    ax.set_title('Hubungan Penjualan Es krim dengan Suhu')
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan")
    ax.grid(True)
    st.pyplot(fig)

def Multiple_scatter():
    st.subheader('Multiple Scatter Plot')
    fig, ax = plt.subplots()
    ax.scatter(suhu,penjualan_weekdays,color='red',marker='o',s=100,edgecolor='black',alpha=0.6, label="Hari Kerja")
    ax.scatter(suhu,penjualan_weekends,color='green',marker='o',s=100,edgecolor='black',alpha=0.6, label="Akhir Pekan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel("Penjualan")
    ax.grid(True)
    st.pyplot(fig)


def analisis_scatter():
    st.subheader('Analisis Scatter Plot')
    
    jenis_eskrim= st.selectbox('pilih jenis eskrim', ['Cokelat','Vanila','Strawberi'])

    if jenis_eskrim =='Cokelat':
        penjualan = df['penjualan_Cokelat']
    elif jenis_eskrim =='Vanila':
        penjualan = df['penjualan_Vanila']
    elif jenis_eskrim =='Strawberi':
        penjualan = df['penjualan_Strawberi']

    st.subheader("data penjualan dan suhu")
    st.dataframe(df)
    fig, ax = plt.subplots()
    scatter = ax.scatter(df['suhu'],penjualan,c=df['kelembapan'],marker="X", cmap="coolwarm",alpha=0.6)
    ax.set_title(f"Gubungan penjualan {jenis_eskrim} vs suhu dan kelembapan")
    ax.set_xlabel("Suhu")
    ax.set_ylabel(f"Penjualan eskrim {jenis_eskrim}")
    fig.colorbar(scatter, label='Kelembapan (%)')

    st.pyplot(fig)
    st.write(f'grafik menunukan hubungan antara suhu, kelembapan, dan penjualan jenis eskrim ** {jenis_eskrim}** ')

if option == 'Basic Scatter Plot':
    basic_scatter()
if option == 'Kustomisasi Scatter Plot':
    Kustomisasi_scatter()
if option == 'Multiple Scatter PLot':
    Multiple_scatter()
if option == 'Analisis Scatter Plot':
    analisis_scatter()
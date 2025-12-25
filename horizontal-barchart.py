import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 


st.title('Praktikum 6')
st.markdown(""" 
Kelompok 23 :
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
            
""")

#dataset

brands = ['Samsung','Iphone','Poconk','KinkFinix']
sales_2023 = [120,230,170,400]
sales_2024 = [150,200,180,450]
sales_2025 = [170,250,200,480]


y = np.arange(len(brands))
width = 0.4

kategori = st.selectbox(
    'pilih kategori visiualisasi',
    ['basic chart','Kustomisasi grafik','Multiple chart']
)

if kategori == 'basic chart':
    st.subheader('horizontal bar chart sederhana')
    fig1, ax1, = plt.subplots()
    ax1.set_yticks(y)
    ax1.set_xticklabels(brands)
    ax1.set_title('Horizontal bar chart - 2023')
    ax1.set_xlabel('Jumlah Penjualan')
    ax1.set_ylabel('Merk')
    ax1.barh(brands, sales_2023, color='skyblue')
    st.pyplot(fig1)

    st.subheader('horizontal stacked bar chart sederhana')
    fig2, ax2, = plt.subplots()
    ax2.set_yticks(y)
    ax2.set_xticklabels(brands)
    ax2.set_title('Horizontal bar chart - 2023')
    ax2.set_xlabel('Jumlah Penjualan')
    ax2.set_ylabel('Merk')
    ax2.barh(brands, sales_2023, color='skyblue', label='2023')
    ax2.barh(brands, sales_2024, color='lightgreen', label='2024', left=sales_2023)
    ax2.legend()
    st.pyplot(fig2)

elif kategori == 'Kustomisasi grafik':
    st.subheader('Kustomisasi Horizontal bar chart')
    fig3, ax3, = plt.subplots()
    ax3.set_yticks(y)
    ax3.set_xticklabels(brands)
    ax3.set_title('Kustomisasi Horizontal stacked bar chart - 2023')
    ax3.set_xlabel('Jumlah Penjualan')
    ax3.set_ylabel('Merk')
    ax3.barh(brands, sales_2023, color='skyblue', label='2023', edgecolor='black')
    ax3.grid(axis='x',linestyle='--', alpha=0.6)

    for i, v in enumerate(sales_2023):
        ax3.text(v+5, i, str(v), va='center')

    st.pyplot(fig3)

    st.subheader('Kustomisasi horizontal stacked bar chart sederhana')
    fig4, ax4, = plt.subplots()
    ax4.set_yticks(y)
    ax4.set_xticklabels(brands)
    ax4.set_title('Kustomisasi Horizontal stacked bar chart - 2023')
    ax4.set_xlabel('Jumlah Penjualan')
    ax4.set_ylabel('Merk')
    ax4.barh(brands, sales_2023, color='skyblue', label='2023')
    ax4.barh(brands, sales_2024, color='lightgreen', label='2024', left=sales_2023)
    ax4.grid(axis='x',linestyle='--', alpha=0.6)
    st.pyplot(fig4)

else:
    st.subheader('Multiple Horizontal bar chart')
    fig5, ax5, = plt.subplots()
    ax5.set_yticks(y)
    ax5.set_xticklabels(brands)
    ax5.set_title('Multiple Horizontal stacked bar chart - 2023')
    ax5.set_xlabel('Jumlah Penjualan')
    ax5.set_ylabel('Merk')
    ax5.barh(y - width/2, sales_2023,height=width, color='skyblue', label='2023', edgecolor='black')
    ax5.barh(y + width/2, sales_2024,height=width, color='skyblue', label='2023', edgecolor='black')
    ax5.grid(axis='x',linestyle='--', alpha=0.6)
    ax5.legend()
    st.pyplot(fig5)

    st.subheader('Multiple horizontal stacked bar chart sederhana')
    fig6, ax6, = plt.subplots()
    ax6.set_yticks(y)
    ax6.set_xticklabels(brands)
    ax6.set_title('Multiple Horizontal stacked bar chart - 2023')
    ax6.set_xlabel('Jumlah Penjualan')
    ax6.set_ylabel('Merk')
    ax6.barh(brands, sales_2023, color='skyblue', label='2023')
    ax6.barh(brands, sales_2024, color='lightgreen', label='2024', left=sales_2023)
    ax6.legend()
    st.pyplot(fig6)
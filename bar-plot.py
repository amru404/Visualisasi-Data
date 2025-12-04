import streamlit as st
import matplotlib.pyplot as plt
import pandas as pd 

# Streamlit layout
st.title("Visualisasi Data Mahasiswa")
# st.sidebar.header("Pengaturan Grafik")
# option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
#                              ("Line Plot", 
#                               "Kustomisasi Line Plot", 
#                               "Garis Berbeda untuk Menunjukkan Trend",
#                               "Subplot"))
#identitas Kelompok
st.caption('Praktikum 4 - Matplotlib Bar Chart')
st.markdown(""" 
Kelompok 23 :
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
            
""")


# Sample data
data = {
    'Jurusan' : ['Ilmu Komputer','Sistem Informasi','Teknik Informatika','Teknologi Informasi'],
    'Jumlah Mahasiswa' : [120,150,100,80]
}
df = pd.DataFrame(data)

st.title("bar Chart - Jumlah Mahasiswa per Jurusan")
st.bar_chart(df.set_index('Jurusan'))

st.title("Basic Bar Chart Menggunakan Matplotlib")
fig, ax = plt.subplots()
ax.bar(df['Jurusan'], df['Jumlah Mahasiswa'], color='skyblue')
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('JUmlah Mahasiswa')

st.pyplot(fig)

st.title("Kustomisasi Bar Chart")
fig2, ax2 = plt.subplots()
colors = ['blue','green','orange','red']
bars = ax.bar(df['Jurusan'], df['Jumlah Mahasiswa'], color=colors)
ax.set_title('Jumlah Mahasiswa Per Jurusan')
ax.set_xlabel('Jurusan')
ax.set_ylabel('JUmlah Mahasiswa')

for bar in bars:
    ax.text(bar.get_x() + bar.get_width() / 2, bar.get_height() + 5, str(bar.get_height()), ha='center')

st.pyplot(fig)

st.title("multiple bar chart")

data_2023 = [120,150,100,80]
data_2024 = [140,160,120,90]

x = range(len(data['Jurusan']))
width = 0.4

fig,ax = plt.subplots()
ax.bar(x, data_2023, width=width, label='2023',color='skyblue')
ax.bar([p + width/2 for p in x], data_2024, width=width, label="2024", color='pink')
ax.set_title = ('Jumlah Mahasiswa Per Jurusan (2023 vs 2024)')
ax.set_xlabel = ('Jurusan')
ax.set_ylabel = ('JUmlah Mahasiswa')
ax.set_xticks([p + width /2 for p in x])
ax.set_xticklabels(data['Jurusan'])
ax.legend()

st.pyplot(fig)
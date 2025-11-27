import streamlit as st
import matplotlib.pyplot as plt

# Sample data
months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
product_A_sales = [10, 20, 15, 25, 30, 45, 40, 50, 60, 55, 65, 70]
product_B_sales = [5, 10, 8, 15, 18, 20, 22, 30, 25, 35, 40, 45]

# Streamlit layout
st.title("Visualisasi Penjualan Produk")
st.sidebar.header("Pengaturan Grafik")
option = st.sidebar.selectbox("Pilih Tipe Visualisasi", 
                             ("Line Plot", 
                              "Kustomisasi Line Plot", 
                              "Garis Berbeda untuk Menunjukkan Trend",
                              "Subplot"))
#identitas Kelompok
st.caption('Praktikum 3 - Matplotlib Line Chart')
st.markdown(""" 
Kelompok 27 :
    - Amru Abdurrahman Azzam - 0110122322
    - Hayatunnisa - 0110222118
    - Nurul Maedatul Awaliah - 0110122222
            
""")
#Single Line Plot
def line_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label= "Priduct A",)
    ax.set_title('Penjualan Produk A Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    # ax.show()
    st.pyplot(fig)

def trend_lines_plot():
    fig, ax = plt.subplots()
    ax.plot(months, product_A_sales, label='Product A', linestyle='--', color='blue', marker='x')
    ax.plot(months, product_B_sales, label='Product B', linestyle='-', color='red', marker='o')
    ax.set_title('Tren Penjualan Produk Per Bulan')
    ax.set_xlabel('Bulan')
    ax.set_ylabel('Jumlah Penjualan')
    ax.legend()
    ax.grid(True)
    st.pyplot(fig)

def subplots():
    fig, axs = plt.subplots(2, 1, figsize=(10, 8))

    # Plot for Product A
    axs[0].plot(months, product_A_sales, label='Product A', color='blue', marker='o')
    axs[0].set_title('Penjualan Produk A Per Bulan')
    axs[0].set_xlabel('Bulan')
    axs[0].set_ylabel('Jumlah Penjualan')
    axs[0].legend()
    axs[0].grid(True)

    # Plot for Product B
    axs[1].plot(months, product_B_sales, label='Product B', color='red', marker='x')
    axs[1].set_title('Penjualan Produk B Per Bulan')
    axs[1].set_xlabel('Bulan')
    axs[1].set_ylabel('Jumlah Penjualan')
    axs[1].legend()
    axs[1].grid(True)

    plt.tight_layout()
    st.pyplot(fig)

if option == "Line Plot":
    line_plot()
elif option == "Garis Berbeda untuk Menunjukkan Trend":
    trend_lines_plot()
elif option == "Subplot":
    subplots()
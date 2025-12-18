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
stores = ['Store A','Store B','Store C']
male = [150,200,180]
female = [120,230,170]

#data transaksi penjualan
stores = ['Store A','Store B','Store C']
product_a = [200,250,300]
product_b = [150,300,200]

#data quarter
q1_male = [150,180,160]
q1_female = [140,200,180]
q2_male = [170,190,175]
q2_female = [130,210,160]

# 1 grafik stacked vertical bar chart
st.subheader("1. stacked vertical bar chart")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, male, label ='Male', color='#9EC6F3')
ax.bar(x, female, label ='Female', color='#BDDDE4', bottom=male)


ax.set_title('Population by Gender and Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Population')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 2 grafik stacked vertical bar dengan matplotlib
st.subheader("2. stacked vertical bar dengan matplotlib")

fig, ax = plt.subplots()
x = np.arange(len(stores))
ax.bar(x, product_a, label ='Product A', color='#CD5656')
ax.bar(x, product_b, label ='Product B', color='#EAEBD0', bottom=product_a)


ax.set_title('Sales Transaction by Store')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()

st.pyplot(fig)

# 3 grafik Kustomisasi stacked vertical bar chart
st.subheader("3. grafik Kustomisasi stacked vertical bar chart")

for i in range(len(x)):
    plt.text(x[i], product_a[i]/2, str(product_a[i]), ha='center', color="white")
    plt.text(x[i], product_a[i] + product_b[i]/2, str(product_b[i]), ha='center', color="black")
st.pyplot(fig)

# 4 MultipleKustomisasi stacked vertical bar chart
st.subheader("4. Multiple Kustomisasi stacked vertical bar chart")

fig, ax = plt.subplots()
width = 0.4
x = np.arange(len(stores))

ax.bar(x-width/2, q1_male, label='Q1 Male', color='#B7B1F2', width=width)
ax.bar(x-width/2, q1_female, bottom=q1_male, label='Q1 Female', color='#FDB7EA', width=width)

ax.bar(x+width/2, q2_male, label='Q2 Male', color='#FFDCCC', width=width)
ax.bar(x+width/2, q2_female, bottom=q2_male, label='Q2_female Female', color='#FBF3B9', width=width)

ax.set_title('Sales Transaction by Store (Multiple Quarters)')
ax.set_xlabel('Stores')
ax.set_ylabel('Sales')
ax.set_xticklabels(stores)
ax.set_xticks(x)
ax.legend()
st.pyplot(fig)

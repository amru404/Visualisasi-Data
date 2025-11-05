import streamlit as st
import pandas as pd #ngelola data dlm bntuk tabel
import datetime

#text box
st.title("Forms data pribadi") 

nama = st.text_input("Masukan nama") #variable nama untuk nampung isi form

#angka
umur = st.number_input('Masukan umur')

#date
now = datetime.date.today()
tanggal_lahir = st.date_input("pilih tanggal lahir", value=now,
min_value=datetime.date(1930,1,1),
max_value=datetime.date(2025,12,30))

#dataset upload
data_file = st.file_uploader("upload csv", type=["csv"])
details = st.button("check details")
if details:
        if data_file is not None:
            file_details = {"file_name": data_file.name, "file_type":data_file.type, "file_size":data_file.size}
            st.write('file_details')
            df = pd.read_csv(data_file)
            st.dataframe(df)
        else:
            st.write("no csv file is uploaded")

st.write("Nama : ",nama)
st.write("Umur : ",umur)
st.write("Tanggal Lahir : ",tanggal_lahir)

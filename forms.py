import streamlit as st
import pandas as pd #ngelola data dlm bntuk tabel
import numpy as np  #bkin data numb acak
import altair as alt #bkin chart interaktif
import datetime

#text box
st.title("ini text box") 
nama = st.text_input("enter ur name") #variable nama untuk nampung isi form
st.write("your name is", nama)

#teks area
input_text = st.text_area("enter ur address")
st.write("""
your address is 
""", input_text)


#angka
st.number_input('enter the number')

num = st.number_input('enter the number', 0,10,5,2)
st.write("min. value is 0, \n Max is 10")
st.write("default value is 5, \n step size value is 2")
st.write("Total Value after adding number entereed with wtep value is : ", num)

#Time 
st.title("time")
st.time_input("select your time")

#date
st.title("date")
st.date_input("select date")

st.title("date 2")
now = datetime.date.today()
st.date_input("select ur date", value=now,
min_value=datetime.date(2000,1,1),
max_value=datetime.date(2025,12,30))

#color
st.title("select color")
color_code = st.color_picker("select ur color")
st.header(color_code)

#dataset upload
st.title("csv data")
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


#submit button
my_form = st.form(key="form")
a = my_form.text_input(label="enter any text")

submit_button = my_form.form_submit_button(label='submit')

st.write(a)
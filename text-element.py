# import streamlit as st

# #text element
# #header
# st.header("praktikum 1 streamlit")
# st.subheader("ini sub header")
# st.text("ini text biasa")
# st.markdown("**Ini Text Bold** dan *ini text italic*")
# st.markdown(""" 
# - ini baris 1 #bullet list
# 1. ini baris 2 #number list
# * ini baris 3 #bullet list

# """)
# st.caption("ini caption")
# st.title("ini judul")

import streamlit as st

st.title("Praktikum 1 streamlit")
st.subheader("bagian text element")
st.markdown("""
1. Amru Abdurrahman Azzam - 0110122322
2. Hayatunnisa - 0110222118
3. Nurul Maedatul Awaliah 0110122222
""")

#rumus
st.latex(r''' \cos^2\theta = 1-2\sin^2\theta ''') #trigonometri

st.latex(r''' (a+b)^2 = a^2 + b^2 + 2ab ''') #binominal

#kode program
st.header("tampilan code")
st.subheader("py")
#simpan code ke var
codePY = ''' 
def hello():
    print("hello ajam")
'''

st.code(codePY, language = 'python')

st.subheader("java")
st.code(""" 
public class GFG {
    public static void main(string arg[])
    }
""", language = 'java') #bisa buat java c+ html dll

st.subheader("javascript")
st.code("""
<input id="demo" type="text">
<button type="button" onclick="myFunction()">Test Input</button>
<p id="p01"></p>

<script>
function myFunction() {
  const message = document.getElementById("p01");
  message.innerHTML = "";
  let x = document.getElementById("demo").value;
  try { 
    if(x.trim() == "")  throw "empty";
    if(isNaN(x)) throw "not a number";
    x = Number(x);
    if(x < 5)  throw "too low";
    if(x > 10)   throw "too high";
  }
  catch(err) {
    message.innerHTML = "Input is " + err;
  }
}
</script>
""", language = "javascript")
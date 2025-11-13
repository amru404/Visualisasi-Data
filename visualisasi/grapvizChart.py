import streamlit as st
import graphviz as gv

st.title("Graphviz Chart")
st.write("kelompok 23")
st.markdown("""
    1. Amru Abdurrahman Azzam - 0110122322
    2. Hayatunnisa - 0110222118
    3. Nurul Maedatul Awaliah 0110122222
""")

st.graphviz_chart("""
    digraph {
        "Training Data" -> "ML Algorithm"
        "ML Algorithm" -> "Model"
        "Model" -> "Results Forecasting"
        "New Data" -> "Model"
    }
""")


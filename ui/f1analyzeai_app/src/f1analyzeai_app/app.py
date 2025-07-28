# app.py
import streamlit as st
from fastf1_extractor.dummy import dummy_add

st.title("My First Streamlit App")
st.write("Hello, Streamlit with Poetry")
value_x = st.number_input("Enter first number", value=0)
value_y = st.number_input("Enter second number", value=0)
result = dummy_add(value_x, value_y)
st.write(f"The result of adding {value_x} and {value_y} is: {result}")
st.write(
    "This is a simple app to demonstrate the integration of FastF1 Extractor with Streamlit."
)

import streamlit as st 
no = st.slider("choose your number",1,100)
st.write("square of",no," is ",no**2)
import streamlit as st

st.title('Gabriel Thorn')

st.image('images/Gabriel_Thorn.jpg')
with open('text/Gabriel Thorn.txt') as infile:
    st.write(infile.read())
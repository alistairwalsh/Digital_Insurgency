import streamlit as st

st.title('Ren Hayashi')

st.image('images/Ren_Hayashi.jpg')
with open('text/Ren Hayashi.txt') as infile:
    st.write(infile.read())
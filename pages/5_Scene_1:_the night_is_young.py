import streamlit as st

st.title('The night is young')

with open('text/scene_1.txt') as infile:
    st.write(infile.read())
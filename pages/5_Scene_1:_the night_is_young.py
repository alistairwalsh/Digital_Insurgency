import streamlit as st

st.title('The night is young')

st.image('images/Scene_1.jpg')

with open('text/scene_1.txt') as infile:
    st.write(infile.read())
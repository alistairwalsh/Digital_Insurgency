import streamlit as st
import streamlit.components.v1 as components

st.title('A Tangled Web')

st.image('images/character_headshots/Tatiana3.jpg')

with open('text/scene_3.txt') as infile:
    st.write(infile.read())

st.video('https://youtu.be/kRtV9rHn-mo')

st.image('images/character_headshots/Tatiana4.jpg')

import streamlit as st
import streamlit.components.v1 as components

st.title('A Tangled Web')

st.image('images/character_headshots/tatiana3.png')

with open('text/scene_3.txt') as infile:
    st.write(infile.read())

st.video('https://youtu.be/kRtV9rHn-mo')

st.image('images/character_headshots/tatiana4.png')

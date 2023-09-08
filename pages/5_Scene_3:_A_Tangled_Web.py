import streamlit as st
import streamlit.components.v1 as components

st.title('A Tangled Web')

with open('text/scene_3.txt') as infile:
    st.write(infile.read())



st.video('https://youtu.be/kRtV9rHn-mo')

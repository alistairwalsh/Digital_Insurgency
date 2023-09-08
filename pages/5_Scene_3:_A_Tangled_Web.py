import streamlit as st
import streamlit.components.v1 as components

st.title('A Tangled Web')

st.image('images/tatiana3.png')

with open('text/scene_3.txt') as infile:
    st.write(infile.read())

st.video('https://www.tiktok.com/@real_memebrain/video/7276459404470308097?is_from_webapp=1&sender_device=pc&web_id=7235988086685337089')

st.image('images/tatiana4.png')

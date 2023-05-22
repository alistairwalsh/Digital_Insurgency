import streamlit as st

st.title('Nisha Nakamura')

st.image('images/Nisha_Nakamura.jpg')
with open('text/Nisha_Nakamura.txt') as infile:
    st.write(infile.read())

with open('video/Nisha.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

with open('video/87a2237a-4b3f-4775-9e0d-7655c0c0b273.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)
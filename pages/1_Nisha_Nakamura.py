import streamlit as st

st.title('Nisha Nakamura')

st.image('images/Nisha_Nakamura.jpg')
with open('text/Nisha_Nakamura.txt') as infile:
    st.write(infile.read())

video_file = open('video\Nisha.mp4', 'rb')
video_bytes = video_file.read()

st.video(video_bytes)
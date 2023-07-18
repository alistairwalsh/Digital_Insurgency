import streamlit as st

st.title('Scene 2: Nothing is real')

st.image('images/Leonardo_Diffusion_realistic_photo_of_an_angel_with_dark_glass_1.jpg')

with open('video/combined_bitjammer.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

with open('text/scene_2.txt') as infile:
    st.write(infile.read())

with open('video/Nisha, adorned with cybernetic enhancements and a hardened gaze. stands in front of a grimy mirror. wearing nothing but her insecurities. She takes a (1689687422266).mp4') as infile:
    st.write(infile.read())

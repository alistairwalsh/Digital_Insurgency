import streamlit as st

st.title('The night is young')

st.image('images/Scene_1.jpg')

with open('text/scene_1.txt') as infile:
    st.write(infile.read())

with open('video/Scene Setting_ Kent Street Dive Bar, bathed in dim neon lights, throbs with an electric atmosphere. Nisha, beat from her recent runs, seeks solace in -2 (1684566823898).mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0.jpg')


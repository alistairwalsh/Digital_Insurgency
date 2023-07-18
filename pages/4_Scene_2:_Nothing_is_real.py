import streamlit as st

st.title('Scene 2: Nothing is real')

st.image('images/Leonardo_Diffusion_realistic_photo_of_an_angel_with_dark_glass_1.jpg')

with open('video/combined_bitjammer.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

<video controls width="250" autoplay="true" muted="true" loop="true">
<source 
            src="video/combined_bitjammer.mp4" 
            type="video/mp4" />
</video>

with open('text/scene_2.txt') as infile:
    st.write(infile.read())

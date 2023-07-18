import streamlit as st

st.title('Scene 2: Nothing is real')

st.image('images/Leonardo_Diffusion_realistic_photo_of_an_angel_with_dark_glass_1.jpg')

with open('video/combined_bitjammer.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

with open('text/scene_2.txt') as infile:
    st.write(infile.read())

st.video('https://www.tiktok.com/@real_memebrain/video/7257153023456087297?is_from_webapp=1&sender_device=pc&web_id=7235988086685337089')

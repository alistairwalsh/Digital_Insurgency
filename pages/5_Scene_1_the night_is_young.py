import streamlit as st

st.title('The night is young')

st.image('images/Scene_1.jpg')

with open('text/scene_1.txt') as infile:
    st.write(infile.read())

with open('video/Scene Setting_ Kent Street Dive Bar, bathed in dim neon lights, throbs with an electric atmosphere. Nisha, beat from her recent runs, seeks solace in -2 (1684566823898).mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

#st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0.jpg')
#st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_1 (2).jpg')
st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0 (3).jpg')

st.write('Sitting at the bar is a young girl with captivating eyes, lost in thought.' )

st.image('images/PXL_20230702_065835869.PORTRAIT.jpg',width=300)

st.write("Thankyou for letting me use your image, I was so focussed on what I was doing I forgot to get your name - say hi in the comments and I'll add your name to the character. :-).")

with open("text/Amelia Rivers.txt") as infile:
    st.write(infile.read())


import streamlit as st
import streamlit.components.v1 as components

st.title('Kent St')

st.image('images/kent_st.jpg')
components.iframe(src="https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.imgur.com/SdkOUAq.jpg", width=1200, height=700)
components.iframe(src="https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.imgur.com/U4PIoQP.jpg", width=1200, height=700)

components.iframe(src='https://genny.lovo.ai/share/dcfe90a1-fe8b-4a38-a588-b556a8a6e300')

with open('text/the_scene.txt') as infile:
    st.write(infile.read())
st.title('Max')
st.image('images/Max.jpg')
with open('text/Max.txt') as infile:
    st.write(infile.read())

st.title('Jackson')
st.image('images/Jackson.jpg')
with open('text/Jackson.txt') as infile:
    st.write(infile.read())

with open('video/jackson_message.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

components.iframe(src='https://www.kubee.ai/chat?isChange=true&userId=1660580962428149760',  width=800, height=800)

st.title('Lena')
st.image('images/Lena.jpg')
with open('text/lena.txt') as infile:
    st.write(infile.read())

with open('video/Lena, the bar_s resident DJ.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)

with open('video/936fa529-0acd-412a-b5c2-8e1a9eb53888.mp4', 'rb') as infile:
    video_bytes = infile.read()
    st.video(video_bytes)



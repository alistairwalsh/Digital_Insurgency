import streamlit as st
import streamlit.components.v1 as components
from utils import set_page_config, create_sidebar, load_text

set_page_config()
create_sidebar()

st.title('Kent St')

st.image('images/kent_st.jpg')
components.iframe(src="https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.imgur.com/SdkOUAq.jpg", width=1200, height=700)
components.iframe(src="https://renderstuff.com/tools/360-panorama-web-viewer-embed/?image=https://i.imgur.com/U4PIoQP.jpg", width=1200, height=700)

st.header('Narrator')
st.audio('video/2023-06-29_13-07-00.mp3')

st.write(load_text('text/the_scene.txt'))

for character in ['Max', 'Jackson', 'Lena']:
    st.header(character)
    st.image(f'images/{character}.jpg')
    st.write(load_text(f'text/{character}.txt'))
    
    if character == 'Jackson':
        st.video('video/jackson_message.mp4')
    elif character == 'Lena':
        st.video('video/Lena, the bar_s resident DJ.mp4')
        st.video('video/936fa529-0acd-412a-b5c2-8e1a9eb53888.mp4')

components.iframe(src='https://www.kubee.ai/chat?isChange=true&userId=1660580962428149760', width=800, height=800)



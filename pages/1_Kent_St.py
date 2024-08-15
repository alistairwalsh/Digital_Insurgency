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
    image_path = f'images/{character}.jpg'
    if os.path.exists(image_path):
        st.image(image_path)
    else:
        st.write(f"Image for {character} not found.")

    try:
        st.write(load_text(f'text/{character.lower()}.txt'))
    except FileNotFoundError:
        st.write(f"Description for {character} not available.")
    
    if character == 'Jackson':
        if os.path.exists('video/jackson_message.mp4'):
            st.video('video/jackson_message.mp4')
        else:
            st.write("Video for Jackson not found.")
    elif character == 'Lena':
        for video_file in ['video/Lena, the bar_s resident DJ.mp4', 'video/936fa529-0acd-412a-b5c2-8e1a9eb53888.mp4']:
            if os.path.exists(video_file):
                st.video(video_file)
            else:
                st.write(f"Video {video_file} for Lena not found.")

components.iframe(src='https://www.kubee.ai/chat?isChange=true&userId=1660580962428149760', width=800, height=800)



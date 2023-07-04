import streamlit as st

tab1, tab2, tab3 = st.tabs(["Nisha Nakamura", "Ren Hayashi", "Gabriel Thorn"])

with tab1:
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


with tab2:
    st.title('Ren Hayashi')

    st.image('images/Ren_Hayashi.jpg')
    with open('text/Ren Hayashi.txt') as infile:
        st.write(infile.read())


with tab3:
    st.title('Gabriel Thorn')

    st.image('images/Gabriel_Thorn.jpg')
    with open('text/Gabriel Thorn.txt') as infile:
        st.write(infile.read())
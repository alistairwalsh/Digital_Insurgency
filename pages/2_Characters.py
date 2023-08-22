import streamlit as st

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Nisha Nakamura", "Ren Hayashi", "Gabriel Thorn", "Amelia Rivers", 'Xavier "Bitjammer" Voss', 'Adranos Forge'])

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

with tab4:
    st.title('Amelia Rivers')
    st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0 (3).jpg')

    st.write('Sitting at the bar is a young girl with captivating eyes, lost in thought.' )

    st.image('images/PXL_20230702_065835869.PORTRAIT.jpg',width=300)

    st.write("Thankyou for letting me use your image, I was so focussed on what I was doing I forgot to get your name - say hi in the comments and I'll add your name to the character. :-).")

    with open("text/Amelia Rivers.txt") as infile:
        st.write(infile.read())

with tab5:
    st.title('Xavier "Bitjammer" Voss')
    st.image('images/SDXL_09_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_sunlight_0.jpg')

    st.write('Bitjammer sits at the entrance, he is wearing his AI image rig mounted to his chest to capture images of the patrons.' )

    st.image('images/PXL_20230716_050909165.jpg',width=300)

    st.write("Once again Thankyou for letting me use your image, .")

    with open("text/Xavier Bitjammer Voss.txt") as infile:
        st.write(infile.read())

with tab6:
    st.title('Adranos Forge')
    st.image('images/SDXL_09_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_sunlight_0.jpg')





import streamlit as st
import os

def load_character_info(name):
    try:
        with open(f'text/{name}.txt') as infile:
            return infile.read()
    except FileNotFoundError:
        return "Character description not available."

def load_video(path):
    try:
        with open(path, 'rb') as infile:
            return infile.read()
    except FileNotFoundError:
        return None

characters = ["Nisha Nakamura", "Ren Hayashi", "Gabriel Thorn", "Amelia Rivers", 'Xavier "Bitjammer" Voss', 'Adranos Forge', 'Tatiana']

tabs = st.tabs(characters)

for tab, character in zip(tabs, characters):
    with tab:
        st.title(character)
        
        col1, col2 = st.columns([1, 2])
        
        with col1:
            image_path = f'images/{character.replace(" ", "_")}.jpg'
            if os.path.exists(image_path):
                st.image(image_path, use_column_width=True)
            else:
                st.write("Character image not available.")
        
        with col2:
            st.write(load_character_info(character.replace(" ", "_")))
        
        if character == "Nisha Nakamura":
            with st.expander("Watch Nisha's Videos"):
                video1 = load_video('video/Nisha.mp4')
                if video1:
                    st.video(video1)
                video2 = load_video('video/87a2237a-4b3f-4775-9e0d-7655c0c0b273.mp4')
                if video2:
                    st.video(video2)

        if character == "Amelia Rivers":
            st.image('images/DreamShaper_v5_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_di_0 (3).jpg')
            st.write('Sitting at the bar is a young girl with captivating eyes, lost in thought.')
            st.image('images/PXL_20230702_065835869.PORTRAIT.jpg', width=300)
            st.write("Thank you for letting me use your image. I was so focused on what I was doing I forgot to get your name - say hi in the comments and I'll add your name to the character. :-).")

        if character == 'Xavier "Bitjammer" Voss':
            st.image('images/SDXL_09_Scene_Setting_Kent_Street_Dive_Bar_bathed_in_sunlight_0.jpg')
            st.write('Bitjammer sits at the entrance, he is wearing his AI image rig mounted to his chest to capture images of the patrons.')
            st.image('images/PXL_20230716_050909165.jpg', width=300)
            st.write("Once again, thank you for letting me use your image.")

        if character == "Adranos Forge":
            st.image('images/graybeard.png')
            st.write("Beneath the surface, beyond the firm set of his jaw and the steely determination etched into his features, lay a heart forged in loyalty and camaraderie. A sentinel like no other, Adranos Forge was not just a guardian of gates and systems, but a steadfast friend to the hackers who walked the razor's edge between the real and the digital.")
            st.image('images/00016-3669535562.png')

        if character == "Tatiana":
            st.image('images/tatiana2.png')

        if st.button(f"Learn more about {character}"):
            st.write("Here you can add more detailed information or interactions.")
             


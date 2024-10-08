import streamlit as st
import os
from utils import load_text

st.title('Characters')

def load_character_info(name):
    try:
        return load_text(f'text/character_descriptions/{name}.txt')
    except FileNotFoundError:
        return "Character description is not available."
            

def get_file_name(character):
    return character.replace(" ", "_")

characters = ["Nisha_Nakamura", "Ren_Hayashi", "Gabriel_Thorn", "Amelia_Rivers", 'Xavier_Bitjammer_Voss', 'Jackson', 'Max', 'Lena', 'Tatiana']

for character in characters:
    with st.expander(character):
        col1, col2 = st.columns([1, 2])
        
        with col1:
            image_path = f'images/character_headshots/{get_file_name(character)}.jpg'
            if os.path.exists(image_path):
                st.image(image_path, use_column_width=True)
            else:
                st.write("Character image not available.")
        
        with col2:
            info = load_character_info(get_file_name(character))
            sections = info.split("###")
            for section in sections:
                if section.strip():
                    parts = section.split(":", 1)
                    if len(parts) == 2:
                        title, content = parts
                        st.subheader(title.strip())
                        st.write(content.strip())
                    else:
                        st.write(section.strip())
        
        if character == "Nisha_Nakamura":
            st.video('video/Nisha.mp4')
            st.video('video/87a2237a-4b3f-4775-9e0d-7655c0c0b273.mp4')

        if character == "Amelia_Rivers":
            st.image('images/character_headshots/amelia_4.jpg')
            st.write('Sitting at the bar is a young girl with captivating eyes, lost in thought.')
            st.image('images/character_headshots/amelia_original.jpg')
            st.image('images/character_headshots/amelia_3.jpg')
            st.write("Thank you for letting me use your image. I was so focused on what I was doing I forgot to get your name - say hi in the comments and I'll add your name to the character. :-).")

        if character == 'Xavier_Bitjammer_Voss':
            st.write('Bitjammer sits at the entrance, he is wearing his AI image rig mounted to his chest to capture images of the patrons.')
            st.image('images/character_headshots/bitjammer_2.jpg')
            st.image('images/character_headshots/bitjammer_original.jpg')
            st.write("Once again, thank you for letting me use your image.")

        if character == 'Tatiana':
            st.image('images/character_headshots/Tatiana.jpg')
            st.image('images/character_headshots/Tatiana3.jpg')
            st.image('images/character_headshots/Tatiana4.jpg')

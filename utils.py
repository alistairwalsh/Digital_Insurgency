import streamlit as st

def set_page_config():
    st.set_page_config(
        page_title="Digital Insurgency",
        page_icon="🌆",
        layout="wide"
    )

def create_sidebar():
    with st.sidebar:
        st.title("Digital Insurgency")
        st.markdown("#### Unleashing the System's Edge")
        
        pages = {
            "Home": "Digital_Insurgency",
            "Kent St": "1_Kent_St",
            "Characters": "2_Characters",
            "Scene 1": "3_Scene_1:_The night_is_young",
            "Scene 2": "4_Scene_2:_Nothing_is_real",
            "Scene 3": "5_Scene_3:_A_Tangled_Web",
            "ChatGPT": "7_ChatGPT",
            "Stable Diffusion": "8_Stable_Diffusion",
            "About": "10_about",
            "Comments": "10_comments"
        }
    
        for page_name, page_file in pages.items():
            if st.button(page_name):
                if page_name == "Home":
                    st.switch_page("Digital_Insurgency.py")
                else:
                    st.switch_page(f"pages/{page_file}.py")

def load_text(file_path):
    with open(file_path, 'r') as file:
        return file.read()

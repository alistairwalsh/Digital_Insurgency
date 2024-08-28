import streamlit as st
import os
from PIL import Image
import json

SAVE_DIR = "generated_images"

st.title("Image Gallery")

st.write("Welcome to the Image Gallery. Here you can view all the AI-generated images and their prompts.")

# Get all image files from the generated_images folder
image_files = [f for f in os.listdir(SAVE_DIR) if f.startswith('output-') and f.endswith('.png')]

if not image_files:
    st.write("No images have been generated yet. Go to the AI Image Generation page to create some!")
else:
    # Display images in a grid
    cols = st.columns(2)
    for idx, image_file in enumerate(sorted(image_files, reverse=True)):
        with cols[idx % 2]:
            image_path = os.path.join(SAVE_DIR, image_file)
            image = Image.open(image_path)
            st.image(image, use_column_width=True)
            
            # Get the corresponding prompt file
            prompt_file = f"prompt-{image_file[7:-4]}.json"
            prompt_path = os.path.join(SAVE_DIR, prompt_file)
            
            if os.path.exists(prompt_path):
                with open(prompt_path, 'r') as f:
                    prompt_data = json.load(f)
                    st.write(f"Prompt: {prompt_data['prompt']}")
            else:
                st.write("Prompt not found.")
            
            # Provide download button for each image
            with open(image_path, "rb") as file:
                btn = st.download_button(
                    label="Download",
                    data=file,
                    file_name=image_file,
                    mime="image/png"
                )
            
            st.write("---")  # Add a separator between images
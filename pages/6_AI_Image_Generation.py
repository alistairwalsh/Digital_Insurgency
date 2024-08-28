import streamlit as st
import requests
from datetime import datetime
from PIL import Image
import io
import os
import json

# Keep the existing API_URL
API_URL = "https://8000-01j6bh3pme1z7gksvmvndnpv69.cloudspaces.litng.ai/predict"

# Create a directory to save generated images
SAVE_DIR = "generated_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def generate_image(prompt):
    response = requests.post(API_URL, json={"prompt": prompt})
    if response.status_code == 200:
        timestamp = datetime.now().strftime('%Y%m%d%H%M%S')
        filename = f"output-{timestamp}.png"
        image = Image.open(io.BytesIO(response.content))
        
        # Save the image
        save_path = os.path.join(SAVE_DIR, filename)
        image.save(save_path)
        
        # Save the prompt
        prompt_file = f"prompt-{timestamp}.json"
        prompt_path = os.path.join(SAVE_DIR, prompt_file)
        with open(prompt_path, 'w') as f:
            json.dump({"prompt": prompt}, f)
        
        return image, filename
    else:
        st.error(f"Error: Response with status code {response.status_code} - {response.text}")
        return None, None

st.title("AI Image Generation")

st.write("Welcome to the AI Image Generation page. Here you can create images using AI based on your text prompts.")

prompt = st.text_input("Enter your image prompt:")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            image, filename = generate_image(prompt)
            if image:
                st.image(image, caption="Generated Image")
                st.success(f"Image generated successfully and saved as {filename}!")
                
                # Provide download button
                buf = io.BytesIO()
                image.save(buf, format="PNG")
                btn = st.download_button(
                    label="Download Image",
                    data=buf.getvalue(),
                    file_name=filename,
                    mime="image/png"
                )
    else:
        st.warning("Please enter a prompt before generating an image.")

st.write("Note: Make sure your Flux server is running at the specified API_URL before generating images.")
st.write("Generated images are saved in the 'generated_images' folder along with their prompts.")
st.write("You can view all generated images and their prompts in the Image Gallery page.")
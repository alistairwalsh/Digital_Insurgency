import streamlit as st
import requests
from datetime import datetime
from PIL import Image
import io
import os
import json

# Update the API_URL to use port 8000
API_URL = "https://8000-01j6bh3pme1z7gksvmvndnpv69.cloudspaces.litng.ai:8000/predict"

# Create a directory to save generated images
SAVE_DIR = "generated_images"
os.makedirs(SAVE_DIR, exist_ok=True)

def generate_image(prompt):
    try:
        response = requests.post(API_URL, json={"prompt": prompt}, timeout=10)
        response.raise_for_status()  # Raises an HTTPError for bad responses
        
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
        
        return image, filename, "success"
    except requests.exceptions.RequestException as e:
        return None, None, f"Error: {str(e)}"

st.title("AI Image Generation")

st.write("Welcome to the AI Image Generation page. Here you can create images using AI based on your text prompts.")

prompt = st.text_input("Enter your image prompt:")

if st.button("Generate Image"):
    if prompt:
        with st.spinner("Generating image..."):
            image, filename, status = generate_image(prompt)
            if status == "success":
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
                st.error(f"Failed to generate image. {status}")
    else:
        st.warning("Please enter a prompt before generating an image.")

# Server status indicator
try:
    response = requests.get(API_URL.replace("/predict", ""), timeout=5)
    if response.status_code == 200:
        st.success("✅ Image generation server is online and responding.")
    else:
        st.warning(f"⚠️ Image generation server is online but returned status code {response.status_code}.")
except requests.exceptions.RequestException:
    st.error("❌ Image generation server is offline or not responding.")

st.write("Note: Generated images are saved in the 'generated_images' folder along with their prompts.")
st.write("You can view all generated images and their prompts in the Image Gallery page.")
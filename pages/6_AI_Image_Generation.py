import streamlit as st
import requests
from datetime import datetime
from PIL import Image
import io

# Update this URL to your server's URL if hosted remotely
API_URL = "https://8000-01j6bh3pme1z7gksvmvndnpv69.cloudspaces.litng.ai/predict"

def generate_image(prompt):
    response = requests.post(API_URL, json={"prompt": prompt})
    if response.status_code == 200:
        filename = f"output-{datetime.now().strftime('%Y%m%d%H%M%S')}.png"
        image = Image.open(io.BytesIO(response.content))
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
                st.success(f"Image generated successfully!")
                
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
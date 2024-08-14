import streamlit as st
from utils import set_page_config, create_sidebar

set_page_config()
create_sidebar()

st.title('About Digital Insurgency')

st.write("""
This site is an evolving project that combines AI-generated content with interactive storytelling. Here's what you need to know:

- The world and characters are inspired by the cyberpunk writings of William Gibson.
- All text, images, and videos are AI-generated, prompted and directed by human input.
- The site is continuously changing and developing as new content is created.
- You can interact with the AI through the ChatGPT and Stable Diffusion pages.
- We welcome your feedback and ideas in the comments section.

Our next steps include expanding the interactive elements and refining the AI-generated content. Stay tuned for updates!

If you enjoy this site and want to support its development, consider [buying us a coffee](https://ko-fi.com/memebrain).
""")

st.markdown("---")
st.subheader("Technical Details")
st.write("""
- Built with Streamlit
- Utilizes OpenAI's GPT models for text generation
- Uses Stable Diffusion for image creation
- Hosted on [platform name]
""")

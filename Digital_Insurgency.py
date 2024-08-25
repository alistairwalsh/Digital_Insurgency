import streamlit as st
from utils import set_page_config, load_text

set_page_config()

st.title('Digital Insurgency')
st.markdown("### Unleashing the System's Edge")
st.image('images/Digital_Insurgency.jpg', use_column_width=True)

st.write("""
Welcome to the world of Digital Insurgency, a cyberpunk narrative where technology 
and rebellion intertwine. Dive into a future where the lines between reality and 
virtual existence blur, and every choice could tip the balance of power.
""")

col1, col2 = st.columns([2, 1])

with col1:
    st.header('The World', divider='grey')
    st.write(load_text('text/the_world.txt'))

with col2:
    st.header('Key Themes', divider='grey')
    st.markdown("""
    - Cybernetic augmentation
    - Corporate dominance
    - Underground resistance
    - Virtual reality
    - Artificial intelligence
    - Hacking and digital warfare
    """)

st.header('Characters', divider='grey')
st.write("Explore the diverse cast of characters that inhabit this dystopian world.")
st.write("Visit the Characters page to learn more about each individual's story and role in the Digital Insurgency.")

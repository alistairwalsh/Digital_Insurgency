import streamlit as st

st.title('Digital Insurgency')

st.image('images/Digital_Insurgency.jpg')

with open('text/title.txt') as infile:
    title_text = infile.read()
    st.title(title_text)

with open('text/the_world.txt') as infile:
    world_text = infile.read()
    st.write(world_text)


with open('text/storyline.txt') as infile:
    storyline_text = infile.read()
    st.write(storyline_text)

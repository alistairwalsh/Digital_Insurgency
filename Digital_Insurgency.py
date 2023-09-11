import streamlit as st

st.header('Digital Insurgency', divider='grey')
st.header("### Unleashing the System's Edge")
st.image('images/Digital_Insurgency.jpg')

with open('text/the_world.txt') as infile:
    world_text = infile.read()
    st.write(world_text)


with open('text/storyline.txt') as infile:
    storyline_text = infile.read()
    st.write(storyline_text)

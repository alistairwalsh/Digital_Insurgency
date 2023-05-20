import streamlit as st

st.title('Kent St')

st.image('images/kent_st.jpg')

with open('text/the_scene.txt') as infile:
    st.write(infile.read())
st.title('Max')
st.image('images/Max.jpg')
with open('text/Max.txt') as infile:
    st.write(infile.read())

st.title('Jackson')
st.image('images/Jackson.jpg')
with open('text/Jackson.txt') as infile:
    st.write(infile.read())

st.title('Lena')
st.image('images/Lena.jpg')
with open('text/lena.txt') as infile:
    st.write(infile.read())



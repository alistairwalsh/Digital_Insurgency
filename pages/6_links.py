import streamlit as st

with open('links.txt') as infile:

    st.markdown(infile.read())
import streamlit as st

with open('text/links.txt') as infile:

    st.markdown(infile.read())

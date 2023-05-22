
import streamlit as st

#adding a single-line text input widget

name = st.text_input('Enter your name: ', 'name')
comment = st.text_input('What do you think?: ', 'comment')




#displaying the entered text

st.write( name + ':')
st.write(comment)
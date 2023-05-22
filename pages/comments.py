
import streamlit as st

#adding a single-line text input widget

all_comments = []

name = st.text_input('Enter your name: ', 'name')
comment = st.text_input('What do you think?: ', 'comment')

all_comments.append((name,comment))




#displaying the entered text
if all_comments:
    for n,c in all_comments:
        st.write( n + ':')
        st.write(c)
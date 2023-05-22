
import streamlit as st

#adding a single-line text input widget

def on_new():
    all_comments.append(comment)
    for c in all_comments:
        st.write(c)


comment = st.text_input(label='What do you think?: ',on_change(on_new))


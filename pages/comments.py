import streamlit as st

form = st.form("my_form")
form.text_input("Comment")

# Now add a submit button to the form:
form.form_submit_button("Submit")
import streamlit as st

with st.form("my_form"):
   text_val = st.text_input("Comment")
   checkbox_val = st.checkbox("Would come back to see how this goes?")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("comment", text_val, "checkbox", checkbox_val)
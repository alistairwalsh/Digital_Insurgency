import streamlit as st
import pandas as pd

df = pd.DataFrame()

with st.form("my_form"):
   text_val = st.text_input("Comment")
   checkbox_val = st.checkbox("Would come back to see how this goes?")

   # Every form must have a submit button.
   submitted = st.form_submit_button("Submit")
   if submitted:
       st.write("comment:", text_val)
       st.write("checkbox", checkbox_val)
       d = {'comment': [text_val],
            'would_return':[checkbox_val]}
       st.markdown('Thank you for your feedback!')
       df = df.append(d, ignore_index = True)
       open('df.csv', 'w').write(df.to_csv())

st.dataframe(df)

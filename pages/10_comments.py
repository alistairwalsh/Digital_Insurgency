import streamlit as st
import streamlit.components.v1 as components
from utils import set_page_config, create_sidebar

set_page_config()
create_sidebar()

st.title('Comments and Feedback')

st.write("""
We value your thoughts and suggestions! Use the form below to leave a comment or provide feedback.
Your input helps us improve and shape the future of Digital Insurgency.
""")

components.iframe(src="https://docs.google.com/forms/d/e/1FAIpQLSfs4yDOBtcmz2z3n9ameHrA04L2C5AEY1MiXiuWxE68cRcEEg/viewform?embedded=true", width=640, height=584)

st.subheader("Recent Comments")
components.iframe(src="https://docs.google.com/spreadsheets/d/e/2PACX-1vTGS7C9k_UgkK5sTJQuZLQq3LmmmFfe4i5VPAjMBehfFORy4t6DxIGsGwFv65Hy0netMjtqWjA-fbIy/pubhtml?gid=1980846108&amp;single=true&amp;widget=true&amp;headers=false", height=400)

st.markdown('---')
st.markdown('If you enjoy this site and want to support its development, consider [buying us a coffee](https://ko-fi.com/memebrain)')


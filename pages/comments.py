
import streamlit as st

st.write("currently not working - soon!")

wt = ['initialised text']
with watchlist:
    st.header('Watchlist')
     #create 2 columns inside watchlist header
    col1 = st.beta_columns()
    with col1:
        container1 = st.beta_container()
        sym = container1.text_input('for adding')
        add_button = container2.button('add')
        if add_button:
            wt.append(sym)
st.write(wt)


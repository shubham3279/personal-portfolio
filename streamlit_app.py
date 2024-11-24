import streamlit as st


with st.sidebar:
    st.write(
        'Hi, I am Shubham.'
    )

pg = st.navigation([st.Page("page_1.py"), st.Page("page_2.py")])
pg.run()

import streamlit as st
import numpy as np



# App content
st.title("EDUCATION")

# Create tabs
tab1, tab2 = st.tabs(["📈 Chart", "🗃 Data"])

# Generate random data
data = np.random.randn(10, 1)

# Content for the first tab
with tab1:
    st.subheader("A tab with a chart")
    st.line_chart(data)

# Content for the second tab
with tab2:
    st.subheader("A tab with the data")
    st.write(data)

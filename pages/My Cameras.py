from PIL import Image
import streamlit as st

st.set_page_config(page_title="My Cameras", page_icon=":tada:", layout="wide")

st.sidebar.success("Select a page above.")

with st.container():
    st.write("---")
    st.header("Fujifilm X-T2")
    st.write("##")
    col_1, col_2 = st.columns((2))
    with col_1:
        st.write("##")

st.write("---")

with st.container():
    st.write("---")
    st.header("Leica M10-P")
    st.write("##")
    col_1, col_2 = st.columns((2))
    with col_1:
        st.write("##")
        st.write("##")

st.write("---")
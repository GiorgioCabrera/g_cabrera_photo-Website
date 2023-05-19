from PIL import Image
import streamlit as st

image_1 =  Image.open("images/20230327/1.jpg")
image_2 =  Image.open("images/20230527/2.jpg")
image_3 =  Image.open("images/20230527/3.jpg")
image_4 =  Image.open("images/20230527/4.jpg")
image_5 =  Image.open("images/20230527/5.jpg")
image_6 =  Image.open("images/20230527/6.jpg")

st.set_page_config(page_title="2023-05-27", page_icon=":tada:", layout="wide")

st.sidebar.success("Select a page above.")

with st.container():
    st.write("---")
    st.header("Alabang - Philippines")
    st.write("##")
    image_col_1, image_col_2 = st.columns((2    ))
    with image_col_1:
        st.image(image_1, width=800)
    with image_col_2:
        st.image(image_2, width=800)


with st.container():
    st.write("---")
    st.header("Alabang - Philippines")
    st.write("##")
    image_col_1, image_col_2 = st.columns((2    ))
    with image_col_1:
        st.image(image_3, width=800)
    with image_col_2:
        st.image(image_4, width=800)

with st.container():
    st.write("---")
    st.header("Alabang - Philippines")
    st.write("##")
    image_col_1, image_col_2 = st.columns((2    ))
    with image_col_1:
        st.image(image_5, width=800)
    with image_col_2:
        st.image(image_6, width=800)

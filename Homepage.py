import streamlit as st
import glob

st.set_page_config(page_title="My Webpage", page_icon=":tada:", layout="wide")

st.sidebar.success("Select a page above.")

st.title("Welcome to my Homepage")
with st.container():
    st.subheader("Hi, I am Gio :wave:")
    st.write("I am passionate about photography, crossfit and ultimate frisbee")
    st.write("##")

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

# def load_images():
#     image_files = glob.glob("images/*.jpg")
#     manuscripts = []
#     for image_file in image_files:
#         image_file = image_file.replace("\\", "/")
#         parts = image_file.split("/")
#         if parts[1] not in manuscripts:
#             manuscripts.append(parts[1])
#         manuscripts.sort()
#
#     return image_files, manuscripts
# image_files, manuscripts = load_images()
# n = st.number_input("Select Grid Width", 1, 7, 5)
#
# view_images = []
# for image_file in image_files:
#     view_images.append(image_file)
# groups = []
# for i in range(0, len(view_images), n):
#     groups.append(view_images[i:i + n])
#
# for group in groups:
#     cols = st.columns(n)
#     for i, image_file in enumerate(group):
#         cols[i].image(image_file)
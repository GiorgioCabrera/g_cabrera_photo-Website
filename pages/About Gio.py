import streamlit as st

st.set_page_config(page_title="About Gio", page_icon=":tada:", layout="wide")

st.sidebar.success("Select a page above.")

with st.container():
    st.write("---")
    st.header("Personal Profile")
    st.write("##")
    col_1, col_2 = st.columns(2)
    with col_1:
        st.write("I am a PhD graduate from the Business School of the University of Strathclyde in the departments of "
                 "Management Science and Economics. My PhD focused on investigating the economic feasibility of Carbon "
                 "Capture and Storage, a mitigation strategy to reduce carbon emission in power plants and industrial "
                 "facilities at a micro-economic level. During my PhD I have gained deep knowledge using micro-economic "
                 "techniques, economic modelling and industrial organization theory to replicate a real-life world problem "
                 "and find a solution for it in order to influence the relevant decision-makers to achieve a better choice.")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Currently I am a Consultant for Techmodal, an expert consultancy firm working across"
                 " Defence, Commercial and Public Sectors solving complex problems. My other skills also include excellent"
                 " organization, planning and communication skills - especially the fact I am a multilingual individual "
                 "who can speak 3 languages fluently - English, Italian and Tagalog.")

with st.container():
    col1, col2 = st.columns(2)
    with col1:
        st.write("Currently I am a Consultant for Techmodal, an expert consultancy firm working across"
                 " Defence, Commercial and Public Sectors solving complex problems. My other skills also include excellent"
                 " organization, planning and communication skills - especially the fact I am a multilingual individual "
                 "who can speak 3 languages fluently - English, Italian and Tagalog.")

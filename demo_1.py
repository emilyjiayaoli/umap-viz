import streamlit as st

st.title("Hello world!")

echo = st.button("Echo")
if echo:
    st.write("Echo")

    echo2 = st.button("Echo echo")
    if echo2: #if 
        st.write("Echo echo1")
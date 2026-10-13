import streamlit as st

st.set_page_config(
    page_title="Python 3.15 App",
    page_icon="🐍",
    layout="centered"
)

st.title("🐍 My Python Application")

st.write("Welcome! Your Streamlit app is running.")

name = st.text_input("Enter your name")

if st.button("Submit"):
    if name.strip():
        st.success(f"Hello, {name}! Your app is working.")
    else:
        st.warning("Please enter your name.")

st.divider()
st.write("Built with Python and Streamlit")
import streamlit as st

st.title("leanguage selector box")

language = ["English", "Hindi", "French", "Spanish", "German"]
selected_language = st.selectbox("Select your language", language)


st.write(f"You have selected: {selected_language}")



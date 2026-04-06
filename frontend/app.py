import streamlit as st
import requests

st.title("Skin Disease Detection")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "png", "jpeg"])

if uploaded_file:
    if st.button("Analyze"):
        files = {"file": uploaded_file.getvalue()}

        response = requests.post(
            "http://127.0.0.1:8000/api/v1/skin/analyze",
            files={"file": uploaded_file}
        )

        st.json(response.json())
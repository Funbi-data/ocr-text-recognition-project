import streamlit as st
import pytesseract
from PIL import Image

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

st.title("Funbi OCR App")

uploaded_file = st.file_uploader(
    "Upload an image",
    type=["png", "jpg", "jpeg"]
)

if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption="Uploaded Image")

    if st.button("Extract Text"):

        text = pytesseract.image_to_string(image)

        st.subheader("Detected Text")
        st.write(text)

        st.subheader("Statistics")

        word_count = len(text.split())
        char_count = len(text)

        st.write(f"Words: {word_count}")
        st.write(f"Characters: {char_count}")

        st.download_button(
            "Download Text",
            text,
            file_name="ocr_output.txt"
        )
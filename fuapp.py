import streamlit as st

# File Processing Packages
from PIL import Image
import pandas as pd
import docx2txt

# Import textract
from PyPDF2 import PdfFileReader
import pdfplumber

# Load Images
@st.cache
def load_image(image_file):
    img = Image.open(image_file)
    return img

def read_pdf(file):
    pdfReader = PdfFileReader(file)
    count = pdfReader.numPages
    all_page_text = ""
    for i in range(count):
        page = pdfReader.getPage(i)
        all_page_text += page.extractText()
    
    return all_page_text


def main():
    st.title("File Upload Tutorial")
    
    menu = ["Home","Dataset","DocumentFiles","About"]
    choice = st.sidebar.selectbox("Menu",menu)
    
    if choice == "Home":
        st.subheader("Home")
        image_file = st.file_uploader("Upload Images",
			type=["png","jpg","jpeg"])
        if image_file is not None:
            # To See details
            st.write(type(image_file))
			  # Methods/Attrib
			  # st.write(dir(image_file))
    
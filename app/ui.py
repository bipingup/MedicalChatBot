import streamlit as st

def pdf_uploader():
    st.title("PDF Uploader")
    uploaded_file = st.file_uploader("Choose PDF files", type=["pdf"], accept_multiple_files=True,
                                      help="Upload one or more PDF files to process.")
    if uploaded_file is not None:
        st.success("file uploaded successfully")
    return uploaded_file
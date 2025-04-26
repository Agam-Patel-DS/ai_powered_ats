from .file_handler import read_file

def extract_text(uploaded_file):
    return read_file(uploaded_file)

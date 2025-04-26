import pdfplumber
import docx

def read_pdf(file):
    text = ''
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() + ' '
    return text

def read_docx(file):
    doc = docx.Document(file)
    text = ' '.join([para.text for para in doc.paragraphs])
    return text

def read_file(file):
    if file.name.endswith('.pdf'):
        return read_pdf(file)
    elif file.name.endswith('.docx'):
        return read_docx(file)
    else:
        raise ValueError("Unsupported file type. Only PDF and DOCX allowed.")

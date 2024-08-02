import PyPDF2
import docx2txt

def extract_text_from_files(uploaded_file):
    if uploaded_file.type == "application/pdf":
        return extract_text_from_pdf(uploaded_file)
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(uploaded_file)
    elif uploaded_file.type == "text/plain":
        return extract_text_from_txt(uploaded_file)
    else:
        return ""

def extract_text_from_pdf(uploaded_file):
    reader = PyPDF2.PdfReader(uploaded_file)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text.split('\n\n')

def extract_text_from_docx(uploaded_file):
    text = docx2txt.process(uploaded_file)
    return text.split('\n\n')

def extract_text_from_txt(uploaded_file):
    text = uploaded_file.read().decode("utf-8")
    return text.split('\n\n')

import os
import PyPDF2
import docx

def read_text_file(file_path):
    """Read content from a text file."""
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as file:
        return file.read()

def read_pdf_file(file_path):
    """Extract text from a PDF file."""
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ''
        for page in range(len(reader.pages)):
            text += reader.pages[page].extract_text()
        return text

def read_docx_file(file_path):
    """Extract text from a DOCX file."""
    doc = docx.Document(file_path)
    text = ''
    for paragraph in doc.paragraphs:
        text += paragraph.text
    return text

def search_in_file(file_path, search_term):
    """Search for a term in the file's content."""
    _, ext = os.path.splitext(file_path)
    ext = ext.lower()

    try:
        if ext == '.txt':
            content = read_text_file(file_path)
        elif ext == '.pdf':
            content = read_pdf_file(file_path)
        elif ext == '.docx':
            content = read_docx_file(file_path)
        else:
            return False  # Only support certain file types

        # Search for the term (case insensitive)
        return search_term.lower() in content.lower()

    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return False

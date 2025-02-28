import os
from PyPDF2 import PdfReader

def load_ducs(path: str) -> list:
    ducs , filenames = [], []

    for duc_file in os.listdir(path):
        if duc_file.endswith(".pdf"):
            duc_path = os.path.join(path,  duc_file)
            with open(duc_path, "rb") as file:
                reader = PdfReader(file)
                text = ""
                for page in reader.pages:
                    text += page.extract_text()
                ducs.append(text)
                filenames.append(duc_file)
    
    return ducs, filenames
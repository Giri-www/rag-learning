""" 
Document Loader 

Specially designed for loading multiple documents.

"""

import os 
from pypdf import PdfReader
# import doc
import pandas as pd


class DocumentLoader: 

    def __init__(self,folder="data"):
        self.folder = folder

    #!-- PDF Loader
    def load_pdf(self,path,file):
        documents = []
        reader = PdfReader(path)

        for page_num,page in enumerate(reader.pages):
            text = page.extract_text()
            documents.append(
                {
                   "text":text,
                   "source":file,
                   "page_num":page_num + 1,

                }

            )

        return documents

    #! -- TXT Loader -- 
    def load_txt(self,path,file):
        with open (path,"r",encoding="utf-8") as f:
            text = f.read()
        return [
            {
                "text":text,
                "source":file,
                # "page_num":1,
            }
        ]

    #! -- CSV LOADER --
    def load_csv(self,path,file):
        df = pd.read_csv(path)
        return [
            {
                "text":df.to_string(),
                "source":file,
                # "page_num":1,
            }
        ]

    #! MAIN LOADER 

    def load_documents(self):
        documents = []

        for file in  os.listdir(self.folder):
            path = os.path.join(self.folder,file)

        if file.endswith(".pdf"):
            documents.extend(self.load_pdf(path,file))
        elif file.endswith(".docx"):
            documents.extend(self.load_docx(path,file))
        elif file.endswith(".txt"):
            documents.extend(self.load_txt(path,file))
        elif file.endswith(".csv"):
            documents.extend(self.load_csv(path,file))

        return documents

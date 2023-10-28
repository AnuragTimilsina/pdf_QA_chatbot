import os 
import pickle
from pathlib import Path
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


with open("API_key") as f:
    key = str(f.readline()).strip()
    print(key)
    os.environ["OPENAI_API_KEY"] = key


# Define a function named read_pdf_texts that takes a folder path as input:
def read_pdf_texts(pdf_folder): 

    # Initialize an empty list to store the extracted text from all PDF files: 
    pdf_texts = []
    pass



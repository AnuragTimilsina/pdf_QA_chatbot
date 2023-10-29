import os 
import pickle
from pathlib import Path
from PyPDF2 import PdfReader
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI


with open("./pdfs/API_key") as f:
    key = str(f.readline()).strip()
    print(key)
    os.environ["OPENAI_API_KEY"] = key


# Define a function named read_pdf_texts that takes a folder path as input:
def read_pdf_texts(pdf_folder): 

    # Initialize an empty list to store the extracted text from all PDF files: 
    pdf_texts = []
    
    for pdf_file in Path(pdf_folder).glob('*.pdf'):
        with open(pdf_file, 'rb') as f: 
            reader = PdfReader(f)

            raw_text = ''

            # Iterate over all the pages in the PDF file and extract the text from each page
            for i, page in enumerate(reader.pages):
                text = page.extract_text()
                if text: 
                    raw_text += text 

            pdf_texts.append(raw_text)

    return pdf_texts


# Construct or load existing embeddings: 
def get_embeddings(): 

    # check if the embeddings.pkl file already exists in the current dir. 
    if os.path.isfile("embeddings.pkl"): 

        # If the file exists, open it in binary mode and load its contents using pickle
        with open("embeddings.pkl", 'rb') as f: 
            pickle.load(f)

    else: 
        # IF the file does not exist, create a new OpenAIEmbeddings object and save it to a new file. 
        embeddings = OpenAIEmbeddings()
        with open("embeddings.pkl", 'wb') as f: 
            pickle.dump(embeddings, f)

        # Return the newly created embeddings object
        return embeddings
    

def main():
    # Prompt user to enter path to PDF folder
    pdf_folder = input("Enter the path to your PDF floder:")
    # Extract text from all PDF files in the folder
    pdf_texts = read_pdf_texts(pdf_folder)

    # Define how to split text into smaller chunks
    text_splitter = CharacterTextSplitter(
        separator="\n", 
        chunk_size=1000,
        chunk_overlap=100,
        length_function=len,
    )

    # Split each PDF's text into smaller chinks and store all chinks in a list. 
    all_texts = []
    for raw_text in pdf_texts: 
        texts = text_splitter.split_text(raw_text)
        all_texts.extend(texts)

    # Load pre_trained word embeddings
    embeddings = get_embeddings()

    # Index the text using the embeddings to enable efficient similarity search
    docsearch = FAISS.from_texts(all_texts, embeddings)

    # Load a pre_trained question answering model 
    # Note: You can specify the model to use by passing the model_name parameter:
    # OpenAI(model_name="text-curie-001"). It will use Davinci by default.
    chain = load_qa_chain(OpenAI(), chain_type="stuff")

    # Enter an infinite loop to prompt the user for questions and generate answers: 
    while True: 
        # Prompt user to enter a question
        query = input("Enter your question (or 'quit' to exit): ")
        # If user enters "Quit", break out of the loop and terminate the program 
        if query.lower() == 'quit':
            break

        # Find the most similar documents in the index to the user's question 
        docs = docsearch.similarity_search(query)
        # Print the IDs of the most similar documents to the console: 
        print(docs)

        # Generate an answer to the user's question using the pre-trained question answeering model
        # by running the model on the selected documents
        answer = chain.run(input_documents=docs, question=query)
        # Print the answer to the console
        print(answer)


if __name__ == "__main__": 
    main()



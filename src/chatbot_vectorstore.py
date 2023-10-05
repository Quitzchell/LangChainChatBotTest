import os
import time

import streamlit as st

from langchain.chat_models import ChatOpenAI
from langchain.embeddings import OpenAIEmbeddings
from langchain import HuggingFaceHub
from langchain.chains import RetrievalQA
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.text_splitter import CharacterTextSplitter
from langchain.vectorstores import FAISS
from langchain.document_loaders import PyPDFLoader
from langchain.llms import GPT4All

from dotenv import load_dotenv

load_dotenv()

# Set API keys
hugging_face_hub_api_key = os.getenv("HUGGINGFACEHUB_API_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

# Create the texts for vectorstore (already in chunks)
loader = PyPDFLoader("../docs/pdfs/hboi_framework.pdf")
pdf = loader.load()

# Split document in chunks
text_splitter = CharacterTextSplitter(chunk_size=1000, chunk_overlap=30, separator="\n")
split_pdf = text_splitter.split_documents(documents=pdf)

# # OpenAI API LLM
# llm = ChatOpenAI(api_key=openai_key, model_name="gpt-3.5-turbo", temperature=0.5) # very fast!

# # HuggingFace Hub LLM -> only text2text and summarisation models
# llm = HuggingFaceHub(repo_id="bofenghuang/vigo-mistral-7b-chat") # fast, but not working with vectorstore
# llm = HuggingFaceHub(repo_id="lmsys/fastchat-t5-3b-v1.0") # fast, but not working with vectorstore

# Local LLMS:  work very slow on cpu, need gpu to speed up
llm = GPT4All(model="D:/Programmeren/Pycharm/LLMS/wizardlm-13b-v1.1-superhot-8k.ggmlv3.q4_0.bin", verbose=True)
# llm = GPT4All(model="D:/Programmeren/Pycharm/LLMS/orca-mini-3b.ggmlv3.q4_0.bin", verbose=True) # more lightweight, but still slow
# llm = GPT4All(model="D:/Programmeren/Pycharm/LLMS/ggml-model-gpt4all-falcon-q4_0.bin", verbose=True)  # more lightweight, but still slow
# uses lots of cpu and memory

# # Create the embeddings
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
# embeddings = OpenAIEmbeddings()

# # Create the vectorstore
# vectorstore = FAISS.from_documents(split_pdf, embedding=embeddings)
# vectorstore.save_local("../docs/vectorstores/openai_hboi_vectorstore")  # when saving new vectorstore
# vectorstore = FAISS.load_local(folder_path="../docs/vectorstores/hboi_framework_vectorstore", embeddings=embeddings)


# vectorstore = FAISS.load_local(folder_path="../docs/vectorstores/openai_hboi_vectorstore", embeddings=embeddings) # need openai embeddings!
vectorstore = FAISS.load_local(folder_path="../docs/vectorstores/hboi_framework_vectorstore",
                               embeddings=embeddings)  # need openai embeddings!


def ask_question(query):
    start_time = time.time()
    qa = RetrievalQA.from_chain_type(llm=llm, chain_type="stuff", retriever=vectorstore.as_retriever())
    result = qa.run(query)
    end_time = time.time()
    elapsed_time = end_time - start_time
    print(f"Elapsed time: {elapsed_time}")
    print(result)


def main():
    query = input("Type in your query: \n")
    while query != "exit":
        ask_question(query)
        query = input("Type in your query: \n")


if __name__ == "__main__":
    main()

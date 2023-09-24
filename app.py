import streamlit as st
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.llms import HuggingFaceHub
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceInstructEmbeddings
from langchain.vectorstores import FAISS
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from htmlTemplate import css, bot_template, user_template


def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text


def get_text_chunks(raw_text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(raw_text)
    return chunks


def get_vectorstore(text_chunks):
    embeddings = HuggingFaceInstructEmbeddings(model_name="hkunlp/instructor-xl")
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    return vectorstore


def get_conversation(vectorstore):
    llm = HuggingFaceHub(repo_id="google/flan-t5-xxl", model_kwargs={"temperature": 0.5, "max_length": 512})
    memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain


def handle_user_question(user_question):
    response = st.session_state.conversation({'question': user_question})
    st.session_state.chat_history = response['chat_history']
    st.write(bot_template.replace("{{MSG}}", response['answer']), unsafe_allow_html=True)


# Application starts here!
def main():
    load_dotenv()
    st.set_page_config(page_title="Chatbot that reads PDFs", page_icon=":eyes:")

    st.write(css, unsafe_allow_html=True)

    if "conversation" not in st.session_state:
        st.session_state.conversation = None
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    st.header(":robot_face: Pretty dumb studybuddy v0.1 :robot_face:")
    user_question = st.text_input("Ask me a question about your documents")
    if user_question:
        handle_user_question(user_question)

    with st.sidebar:
        st.subheader("Documents")
        pdf_docs = st.file_uploader("Upload your document(s) here", accept_multiple_files=True)
        if st.button("Process"):
            with st.spinner("Processing"):
                # get raw pdf text
                raw_text = get_pdf_text(pdf_docs)

                # split the raw_text into chunks
                text_chunks = get_text_chunks(raw_text)

                #  create vector store
                vectorstore = get_vectorstore(text_chunks)

                # conversation chain
                st.session_state.conversation = get_conversation(vectorstore)


if __name__ == '__main__':
    main()

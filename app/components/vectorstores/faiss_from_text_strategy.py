from langchain.vectorstores import FAISS

from app.components.vectorstores.abstract.vectorStore import VectorStore
from app.utils.text_utils import TextExtractor


class FaissFromTextStrategy(VectorStore):
    def __init__(self, path: str, embeddings):
        raw_text = TextExtractor.extract_text_from_pdf(pdf_path=path)
        chunks = TextExtractor.chunk_text(raw_text=raw_text)
        self.vector_store = FAISS.from_texts(texts=chunks, embedding=embeddings)

    def as_retriever(self):
        return self.vector_store.as_retriever()

    def save(self, path: str):
        self.vector_store.save_local(folder_path=path)


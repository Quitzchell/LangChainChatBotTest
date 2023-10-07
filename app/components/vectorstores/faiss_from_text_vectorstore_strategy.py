from langchain.vectorstores import FAISS

from app.components.vectorstores.abstract.vectorStore import VectorStore
from app.utils.text_utils import TextExtractor


class FaissFromTextVectorStoreStrategy(VectorStore):
    def __init__(self, path: str, embeddings):
        raw_text = TextExtractor.extract_text_from_pdf(pdf_path=path)
        chunks = TextExtractor.chunk_text(raw_text=raw_text)
        self.vectorstore = FAISS.from_texts(texts=chunks, embedding=embeddings)

    def as_retriever(self):
        return self.vectorstore.as_retriever()

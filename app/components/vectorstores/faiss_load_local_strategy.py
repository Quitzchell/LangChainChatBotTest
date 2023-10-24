from langchain.vectorstores import FAISS

from app.components.vectorstores.abstract.vectorStore import VectorStore


class FaissLoadLocalStrategy(VectorStore):
    def __init__(self, path: str, embeddings):
        self.vector_store = FAISS.load_local(folder_path=path, embeddings=embeddings)

    def as_retriever(self):
        return self.vector_store.as_retriever()

    def save(self, path: str):
        self.vector_store.save_local(folder_path=path)

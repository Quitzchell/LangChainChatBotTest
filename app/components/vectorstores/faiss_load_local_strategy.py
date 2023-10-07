from langchain.vectorstores import FAISS

from app.components.vectorstores.abstract.vectorStore import VectorStore


class FaissFromTextVectorStoreStrategy(VectorStore):
    def __init__(self, path: str, embeddings):
        self.vectorstore = FAISS.load_local(folder_path=path, embeddings=embeddings)

    def as_retriever(self):
        return self.vectorstore.as_retriever()

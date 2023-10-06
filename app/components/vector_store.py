from langchain.vectorstores import FAISS


class VectorStore:
    def __init__(self, texts: list[str], path: str, embeddings):
        # self.vectorstore = FAISS.load_local(folder_path=path, embeddings=embeddings)
        self.vectorstore = FAISS.from_texts(texts=texts, embedding=embeddings)

    """Add a vector representation for a given text"""
    def add_vector(self, text, vector):
        pass

    """Get the vector representation for a given text"""
    def get_vector(self, text):
        pass

    def as_retriever(self):
        return self.vectorstore.as_retriever()

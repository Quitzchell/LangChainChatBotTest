from langchain.embeddings import HuggingFaceEmbeddings
from app.components.embeddings.abstract.embeddings import Embeddings


class HuggingFaceEmbeddingsStrategy(Embeddings):
    def __init__(self, model_name: str):
        self.embedding = HuggingFaceEmbeddings(model_name=model_name)

    def get_embedding(self):
        return self.embedding

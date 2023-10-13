from abc import ABC, abstractmethod

from app.components.vectorstores.abstract.vectorStore import VectorStore


class LanguageModel(ABC):
    @abstractmethod
    def generate_response(self, question: str, vector_store: VectorStore) -> str:
        pass

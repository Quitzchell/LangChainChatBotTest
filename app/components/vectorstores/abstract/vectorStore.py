from abc import ABC, abstractmethod


class VectorStore(ABC):
    @abstractmethod
    def as_retriever(self):
        pass

    @abstractmethod
    def save(self, path: str):
        pass

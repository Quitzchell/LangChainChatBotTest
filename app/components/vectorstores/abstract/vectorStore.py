from abc import ABC, abstractmethod


class VectorStore(ABC):
    @abstractmethod
    def as_retriever(self):
        pass

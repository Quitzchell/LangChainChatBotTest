from abc import ABC, abstractmethod


class Embeddings(ABC):
    @abstractmethod
    def get_embedding(self):
        pass

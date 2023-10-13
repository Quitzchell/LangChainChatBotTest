from app.components.vectorstores.faiss_from_text_strategy import FaissFromTextStrategy
from app.components.vectorstores.faiss_load_local_strategy import FaissLoadLocalStrategy


class VectorStoreSelector:
    vectorStores = {
        'FaissFromTextStrategy': FaissFromTextStrategy,
        'FaissLoadLocalStrategy': FaissLoadLocalStrategy
    }

    def get_vectorstore(self, key: str):
        return self.vectorStores[key]

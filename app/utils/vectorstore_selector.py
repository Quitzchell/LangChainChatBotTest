from app.components.vectorstores.faiss_from_text_vectorstore_strategy import FaissFromTextVectorStoreStrategy


class VectorStoreSelector:
    vectorStores = {
        'FaissFromTextVectorstoreStrategy': FaissFromTextVectorStoreStrategy
    }

    def get_vectorstore(self, index: str):
        return self.vectorStores.get(index)

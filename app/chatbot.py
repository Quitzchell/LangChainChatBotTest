from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.faiss_from_text_strategy import VectorStore


class Chatbot:
    def __init__(self, language_model: LanguageModel, embeddings: Embeddings, vector_store: VectorStore):
        self.language_model = language_model
        self.embeddings = embeddings # todo: might not need to inject embeddings
        self.vector_store = vector_store

    def answer_question(self, question):
        # Logic to answer a question using the language model and vector store
        response = self.language_model.generate_response(question=question, vector_store=self.vector_store)

        # todo: find out if we need to implement something to persist history

        return response['answer']

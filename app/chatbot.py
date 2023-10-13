from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.faiss_from_text_strategy import VectorStore


class Chatbot:
    def __init__(self, language_model: LanguageModel, vector_store: VectorStore):
        self.language_model = language_model
        self.vector_store = vector_store

    def answer_question(self, question):
        # Logic to answer a question using the language model and vector store
        response = self.language_model.generate_response(question=question, vector_store=self.vector_store)

        # todo: find out if we need to implement something to persist history

        return response

from app.components.embeddings import Embeddings
from app.components.language_model import LanguageModel
from app.components.vector_store import VectorStore


class Chatbot:
    def __init__(self, language_model: LanguageModel, embeddings: Embeddings, vector_store: VectorStore):
        self.language_model = language_model
        self.embeddings = embeddings
        self.vector_store = vector_store
        self.context = {'chat_history': []}

    def answer_question(self, question):
        # Logic to answer a question using the language model and vector store
        response = self.language_model.generate_response(vectorstore=self.vector_store)

        # Add chat history to context
        self.context['chat_history'].append(response['chat_history'])

        print(response)

        # Process the response and return an answer
        # Modify this part based on how you handle the response
        return response

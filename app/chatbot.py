from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.huggingface_hub_language_model_strategy import HuggingFaceHubLanguageModelStrategy
from app.components.vectorstores.faiss_from_text_vectorstore_strategy import VectorStore


class Chatbot:
    def __init__(self, language_model: HuggingFaceHubLanguageModelStrategy, embeddings: Embeddings, vector_store: VectorStore):
        self.language_model = language_model
        self.embeddings = embeddings
        self.vector_store = vector_store
        self.context = {'chat_history': []}

    def answer_question(self, question):
        # Logic to answer a question using the language model and vector store
        response = self.language_model.generate_response(question=question, vectorstore=self.vector_store)
        self.context = response['chat_history']

        # Add chat history to context
        # self.context['chat_history'].append(response['chat_history'])


        # Process the response and return an answer
        # Modify this part based on how you handle the response
        return response['answer']

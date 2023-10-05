import json

from app.chatbot import Chatbot
from app.components.embeddings import Embeddings
from app.components.language_model import LanguageModel
from app.components.vector_store import VectorStore


class ChatbotFactory:
    @staticmethod
    def create_chatbot(config_file_path):
        with open(config_file_path, 'r') as file:
            config = json.load(file)

        # Create language model instance
        language_model = LanguageModel(config["language_model"]["model_name"], config["language_model"]["api_key"])

        # Create embeddings generator
        embeddings = Embeddings(config['model_name'],)

        # Create vector store instance
        vector_store = VectorStore(config["vector_store"]["type"], config["vector_store"]["path"])

        return Chatbot(language_model, embeddings, vector_store)

import json

from app.chatbot import Chatbot
from app.utils.embedding_selector import EmbeddingsSelector
from app.utils.language_model_selector import LanguageModelSelector
from app.utils.vectorstore_selector import VectorStoreSelector


class ChatbotFactory:
    @staticmethod
    def create_chatbot(config_path: str):
        with open(config_path, 'r') as file:
            config = json.load(file)

        # Create embeddings
        embeddings_strategy = config['embeddings']['strategy']
        embeddings_class = EmbeddingsSelector().get_embeddings_class(embeddings_strategy)
        embeddings = embeddings_class(model_name=config['embeddings']['model_name'])

        # Create vector store
        if 'vector_path' in config:
            path = config['vector_store']['vector_path']
            vector_store_strategy = config['vector_store']['local_strategy']
        else:
            path = config['vector_store']['pdf_path']
            vector_store_strategy = config['vector_store']['pdf_strategy']

        vector_store_class = VectorStoreSelector().get_vectorstore(vector_store_strategy)
        vector_store = vector_store_class(
            path=path,
            embeddings=embeddings.get_embedding()
        )

        # Create language model
        language_model_strategy = config['language_model']['strategy']
        language_model_class = LanguageModelSelector().get_language_model_class(language_model_strategy)
        language_model = language_model_class(model_name=config['language_model']['model_name'])

        return Chatbot(language_model, embeddings, vector_store)

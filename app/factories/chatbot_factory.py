import json

from app.chatbot import Chatbot
from app.utils.embedding_selector import EmbeddingsSelector
from app.utils.language_model_selector import LanguageModelSelector
from app.utils.vectorstore_selector import VectorStoreSelector


class ChatbotFactory:
    def create_chatbot(self, config_path: str):
        config = self.load_config(config_path)
        embeddings = self.create_embeddings(config)
        vector_store = self.create_vector_store(config, embeddings)
        language_model = self.create_language_model(config)

        return Chatbot(language_model, embeddings, vector_store)

    def load_config(self, config_path: str):
        with open(config_path, 'r') as file:
            return json.load(file)

    def create_embeddings(self, config):
        embeddings_strategy = config['embeddings']['strategy']
        embeddings_class = EmbeddingsSelector().get_embeddings_class(embeddings_strategy)
        return embeddings_class(model_name=config['embeddings']['model_name'])

    def create_vector_store(self, config, embeddings):
        if 'local_path' in config:
            path = config['vector_store']['local_path']
            vector_store_strategy = config['vector_store']['local_strategy']
        else:
            path = config['vector_store']['pdf_path']
            vector_store_strategy = config['vector_store']['pdf_strategy']

        vector_store_class = VectorStoreSelector().get_vectorstore(vector_store_strategy)
        return vector_store_class(path=path, embeddings=embeddings.get_embedding())

    def create_language_model(self, config):
        language_model_strategy = config['language_model']['strategy']
        language_model_class = LanguageModelSelector().get_language_model_class(language_model_strategy)
        return language_model_class(model_name=config['language_model']['model_name'])


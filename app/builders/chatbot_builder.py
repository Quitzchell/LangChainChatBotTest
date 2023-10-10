import json

from app.chatbot import Chatbot
from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.abstract.vectorStore import VectorStore
from app.utils.embedding_selector import EmbeddingsSelector
from app.utils.language_model_selector import LanguageModelSelector
from app.utils.vectorstore_selector import VectorStoreSelector


class ChatbotBuilder:
    def __init__(self, config_path: str):
        self.config = self.load_config(config_path)

    def build(self) -> Chatbot:
        embeddings = self.create_embeddings()
        vector_store = self.create_vector_store(embeddings)
        language_model = self.create_language_model()

        return Chatbot(language_model, vector_store)

    def load_config(self, config_path: str):
        with open(config_path, 'r') as file:
            return json.load(file)

    def create_embeddings(self) -> Embeddings:
        embeddings_strategy = self.config['embeddings']['strategy']
        embeddings_class = EmbeddingsSelector().get_embeddings_class(embeddings_strategy)
        return embeddings_class(model_name=self.config['embeddings']['model_name'])

    def create_vector_store(self, embeddings) -> VectorStore:
        if 'local_path' in self.config:
            path = self.config['vector_store']['local_path']
            vector_store_strategy = self.config['vector_store']['local_strategy']
        else:
            path = self.config['vector_store']['pdf_path']
            vector_store_strategy = self.config['vector_store']['local_strategy']

        vector_store_class = VectorStoreSelector().get_vectorstore(vector_store_strategy)
        return vector_store_class(path=path, embeddings=embeddings.get_embedding())

    def create_language_model(self) -> LanguageModel:
        language_model_strategy = self.config['language_model']['strategy']
        language_model_class = LanguageModelSelector().get_language_model_class(language_model_strategy)
        return language_model_class(model_name=self.config['language_model']['model_name'])

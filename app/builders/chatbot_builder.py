import json

from app.chatbot import Chatbot
from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.abstract.vectorStore import VectorStore
from app.utils.collections.embeddings_collection import EmbeddingsCollection
from app.utils.collections.language_model_collection import LanguageModelCollection
from app.utils.collections.vectorstore_collection import VectorStoreCollection
from app.utils.config_utils import ConfigUtils


class ChatbotBuilder:
    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = ConfigUtils.load_config(config_path)

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
        embeddings_class = EmbeddingsCollection().get_embeddings_class(embeddings_strategy)
        return embeddings_class(model_name=self.config['embeddings']['model_name'])

    def create_vector_store(self, embeddings) -> VectorStore:
        if 'local_path' in self.config:
            path = self.config['vector_store']['local_path']
            vector_store_strategy = self.config['vector_store']['local_strategy']
        else:
            path = self.config['vector_store']['pdf_path']
            vector_store_strategy = self.config['vector_store']['pdf_strategy']

        vector_store_class = VectorStoreCollection().get_vectorstore(vector_store_strategy)
        return vector_store_class(path=path, embeddings=embeddings.get_embedding())

    def create_language_model(self) -> LanguageModel:
        language_model_strategy = self.config['language_model']['strategy']
        language_model_class = LanguageModelCollection().get_language_model_class(language_model_strategy)
        return language_model_class(model_name=self.config['language_model']['model_name'])

import os

from app.chatbot import Chatbot
from app.components.embeddings.abstract.embeddings import Embeddings
from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.abstract.vectorStore import VectorStore
from app.utils.collections.embeddings_collection import EmbeddingsCollection
from app.utils.collections.language_model_collection import LanguageModelCollection
from app.utils.collections.vectorstore_collection import VectorStoreCollection
from app.utils.config_utils import ConfigUtils


class ChatbotBuilder:
    EMBEDDINGS_KEY = 'embeddings'
    VECTORSTORE_KEY = 'vectorstore'
    LANGUAGE_MODEL_KEY = 'language_model'

    def __init__(self, config_path: str):
        self.config_path = config_path
        self.config = ConfigUtils.load_config(config_path)

    def build(self) -> Chatbot:
        embeddings = self.create_embeddings()
        vectorstore = self.create_vectorstore(embeddings)
        language_model = self.create_language_model()
        return Chatbot(language_model, vectorstore)

    def create_embeddings(self) -> Embeddings:
        embeddings_strategy = self.config[self.EMBEDDINGS_KEY]['strategy']
        embeddings_class = EmbeddingsCollection().get_embeddings_class(embeddings_strategy)
        return embeddings_class(model_name=self.config[self.EMBEDDINGS_KEY]['model_name'])

    def create_vectorstore(self, embeddings: Embeddings) -> VectorStore:
        vectorstore_config = self.config[self.VECTORSTORE_KEY]

        local_path = os.getcwd() + '/' + vectorstore_config.get('local_path')
        if local_path is not None and os.path.isdir(local_path):
            save = False
            path = local_path
            strategy = vectorstore_config.get('local_strategy')
        else:
            save = True
            path = vectorstore_config.get('pdf_path')
            strategy = vectorstore_config.get('pdf_strategy')

        vectorstore_class = VectorStoreCollection().get_vectorstore(strategy)
        vectorstore = vectorstore_class(path=path, embeddings=embeddings.get_embedding())

        if save:
            local_vectorstore_dir = ConfigUtils.get_filename(vectorstore_config.get('pdf_path'))
            vectorstore_type = vectorstore_config.get('type')
            save_path = os.path.join(
                os.getcwd(),
                'docs',
                'vectorstores',
                vectorstore_type,
                local_vectorstore_dir
            )
            vectorstore.save(save_path)

            local_path = os.path.join(
                'docs',
                'vectorstores',
                vectorstore_type,
                local_vectorstore_dir
            )
            self.config[self.VECTORSTORE_KEY]['local_path'] = local_path
            self.config[self.VECTORSTORE_KEY]['local_strategy'] = 'FaissLoadLocalStrategy'
            ConfigUtils.write_config(config_path=self.config_path, config_data=self.config)

        return vectorstore

    def create_language_model(self) -> LanguageModel:
        language_model_strategy = self.config[self.LANGUAGE_MODEL_KEY]['strategy']
        language_model_class = LanguageModelCollection().get_language_model_class(language_model_strategy)
        return language_model_class(model_name=self.config[self.LANGUAGE_MODEL_KEY]['model_name'])

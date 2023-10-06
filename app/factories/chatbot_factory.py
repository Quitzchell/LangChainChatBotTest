import json

from app.chatbot import Chatbot
from app.components.embeddings import Embeddings
from app.components.language_model import LanguageModel
from app.components.vector_store import VectorStore
from app.utils.text_utils import TextExtractor


class ChatbotFactory:
    @staticmethod
    def create_chatbot(config_path: str):
        with open(config_path, 'r') as file:
            config = json.load(file)

        # Create embeddings
        embeddings = Embeddings(
            model_name=config['embeddings']['model_name']
        )

        # Create document for vector store
        raw_text = TextExtractor.extract_text_from_pdf(pdf_path=config["vector_store"]["file_path"])
        chunks = TextExtractor.chunk_text(raw_text=raw_text)

        vector_path = config["vector_store"]["vector_path"]

        # Create vector store instance
        vector_store = VectorStore(
            texts=chunks,
            path=vector_path,
            embeddings=embeddings.get_embedding()
        )

        # Create language model instance
        language_model = LanguageModel(
            model_name=config["language_model"]["model_name"],
            api_key=config["language_model"]["api_key"],
        )

        return Chatbot(language_model, embeddings, vector_store)

from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.faiss_from_text_strategy import VectorStore


class HuggingFaceHubLanguageModelStrategy(LanguageModel):
    def __init__(self, model_name: str):
        self.llm = HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature": 0.5, "max_length": 512})

    def generate_response(self, question: str, vector_store: VectorStore):
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            memory=memory
        )

        response = conversation_chain({'question': question})

        return response

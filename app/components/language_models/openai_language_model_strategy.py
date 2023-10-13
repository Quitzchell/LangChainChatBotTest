from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.faiss_load_local_strategy import VectorStore


class OpenAiLanguageModelStrategy(LanguageModel):
    def __init__(self, model_name: str):
        self.llm = ChatOpenAI(model_name=model_name, temperature=0.5)

    def generate_response(self, question: str, vector_store: VectorStore) -> str:
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vector_store.as_retriever(),
            memory=memory
        )

        response = conversation_chain.run(question=question)

        return response

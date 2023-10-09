from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain

from app.components.language_models.abstract.language_model import LanguageModel
from app.components.vectorstores.faiss_load_local_strategy import VectorStore


class OpenAiLanguageModel(LanguageModel):
    def __init__(self, model_name: str, openai_key: int):
        self.llm = ChatOpenAI(api_key=openai_key, repo_id=model_name, model_kwargs={"temperature": 0.5})

    """Generate a response given the context and a user question."""
    def generate_response(self, question: str, vectorstore: VectorStore):
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )

        response = conversation_chain({'question': question})

        return response

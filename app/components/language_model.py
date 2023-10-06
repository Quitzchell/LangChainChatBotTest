from langchain.llms import HuggingFaceHub
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain


class LanguageModel:
    def __init__(self, model_name: str, api_key: str):
        self.llm = HuggingFaceHub(repo_id=model_name, model_kwargs={"temperature": 0.5, "max_length": 512})
        self.api_key = api_key

    """Generate a response given the context and a user question."""
    def generate_response(self, vectorstore):
        memory = ConversationBufferMemory(memory_key='chat_history', return_messages=True)

        conversation_chain = ConversationalRetrievalChain.from_llm(
            llm=self.llm,
            retriever=vectorstore.as_retriever(),
            memory=memory
        )
        return conversation_chain

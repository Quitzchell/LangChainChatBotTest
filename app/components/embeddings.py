from langchain.embeddings import HuggingFaceEmbeddings


class Embeddings:

    def __init__(self, model_name):
        self.embedding = HuggingFaceEmbeddings(model_name=model_name)
        # Initialize the embeddings model based on the specified model name or default settings
        # Load pre-trained embeddings model based on the model name

    def get_embedding(self, text):
        embedding_vector = self.embedding.get_embedding(text)
        embedding_list = embedding_vector.tolist()
        return embedding_list

    # Additional methods to handle embeddings-related operations could be added here

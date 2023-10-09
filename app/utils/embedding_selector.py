from app.components.embeddings.huggingface_instruct_embeddings_strategy import HuggingfaceInstructEmbeddingsStrategy
from app.components.embeddings.huggingface_embeddings_strategy import HuggingFaceEmbeddingsStrategy


class EmbeddingsSelector:
    embeddings = {
        'HuggingfaceInstructEmbeddingsStrategy': HuggingfaceInstructEmbeddingsStrategy,
        'HuggingFaceEmbeddingsStrategy': HuggingFaceEmbeddingsStrategy,
    }

    def get_embeddings_class(self, index: str):
        return self.embeddings.get(index)

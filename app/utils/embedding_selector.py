from app.components.embeddings.huggingface_instruct_embeddings_strategy import HuggingfaceInstructEmbeddingsStrategy


class EmbeddingsSelector:
    embeddings = {
        'HuggingfaceInstructEmbeddingsStrategy': HuggingfaceInstructEmbeddingsStrategy,
    }

    def get_embeddings_class(self, index: str):
        return self.embeddings.get(index)

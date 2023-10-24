from app.components.language_models.huggingface_hub_language_model_strategy import HuggingFaceHubLanguageModelStrategy
from app.components.language_models.openai_language_model_strategy import OpenAiLanguageModelStrategy


class LanguageModelCollection:
    language_models = {
        "HuggingFaceHubLanguageModelStrategy": HuggingFaceHubLanguageModelStrategy,
        "OpenAiLanguageModelStrategy": OpenAiLanguageModelStrategy
    }

    def get_language_model_class(self, key: str):
        return self.language_models.get(key)

from app.components.language_models.huggingface_hub_language_model_strategy import HuggingFaceHubLanguageModelStrategy
from app.components.language_models.openai_language_model_strategy import OpenAiLanguageModel


class LanguageModelSelector:
    language_models = {
        "HuggingFaceHubLanguageModelStrategy": HuggingFaceHubLanguageModelStrategy,
        "OpenAiLanguageModel": OpenAiLanguageModel
    }

    def get_language_model_class(self, index):
        return self.language_models[index]

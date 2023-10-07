from app.components.language_models.huggingface_hub_language_model_strategy import HuggingFaceHubLanguageModelStrategy


class LanguageModelSelector:
    language_models = {
        "HuggingFaceHubLanguageModelStrategy": HuggingFaceHubLanguageModelStrategy
    }

    def get_language_model_class(self, index):
        return self.language_models[index]

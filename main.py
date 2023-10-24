import os
from dotenv import load_dotenv
from app.builders.chatbot_builder import ChatbotBuilder
from app.utils.collections.bot_collection import BotCollection

load_dotenv()
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')


if __name__ == "__main__":
    chatbot = None
    while True:
        if not chatbot:
            selected_bot = BotCollection().select_bot()
            script_dir = os.path.dirname(__file__)
            config_path = os.path.join(script_dir, 'app', 'configs', selected_bot)

            builder = ChatbotBuilder(config_path=config_path)
            chatbot = builder.build()

        question = input("Type your question (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break

        answer = chatbot.answer_question(question)
        print("Chatbot's Answer:", answer)

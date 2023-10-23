import os

import dotenv
from dotenv import load_dotenv

from app.builders.chatbot_builder import ChatbotBuilder

# setting api keys as environment variables
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')


if __name__ == "__main__":
    load_dotenv()
    chatbot = None

    # todo: research how to handle lifecycle in a docker container
    while True:
        if not chatbot:
            selected_bot = BotCollection().select_bot()
            script_dir = os.path.dirname(__file__)
            config_path = os.path.join(script_dir, 'app', 'configs', selected_bot)

            # Create the chatbot
            builder = ChatbotBuilder(config_path=config_path)
            chatbot = builder.build()

        # Ask for a question
        question = input("Type your question (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break

        # Get the chatbots answer
        answer = chatbot.answer_question(question)
        print("Chatbot's Answer:", answer)

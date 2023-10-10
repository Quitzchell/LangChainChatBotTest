import os

import dotenv
from dotenv import load_dotenv

from app.builders.chatbot_builder import ChatbotBuilder

# setting api keys as environment variables
OPENAI_API_KEY = os.environ.get('OPENAI_API_KEY')
HUGGINGFACEHUB_API_TOKEN = os.environ.get('HUGGINGFACEHUB_API_TOKEN')


# todo: extract this and make it more extendable
def select_bot():
    bot = None
    while bot not in ['1', '2']:
        print('1: flan t5-xxl, instructor-xl, faiss')
        print('2: open-ai, all-MiniLM-L6-v2, faiss')
        bot = input('Select a bot by select its index: ')
        if bot not in ['1', '2']:
            print('That was not an option...')

    if bot == '1':
        return 'flan_t5-xxl_instructor-xl_faiss.json'
    elif bot == '2':
        return 'open_ai_faiss.json'


if __name__ == "__main__":
    load_dotenv()
    chatbot = None

    # todo: research how to handle lifecycle in a docker container
    while True:
        if not chatbot:
            # todo: create component that let users select which chatbot they want to use for benchmarking
            #   Load the chatbot configuration
            selected_bot = select_bot()
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

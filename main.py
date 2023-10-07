import os

from dotenv import load_dotenv

from app.factories.chatbot_factory import ChatbotFactory

if __name__ == "__main__":
    load_dotenv()
    chatbot = None

    # todo: research how to handle lifecycle in a docker container
    while True:
        if not chatbot:
            # todo: create component that let users select which chatbot they want to use for benchmarking
            # Load the chatbot configuration
            selected_bot = 'flan_t5-xxl_instructor-xl_faiss.json'
            script_dir = os.path.dirname(__file__)
            config_path = os.path.join(script_dir, 'app', 'configs', selected_bot)

            # Create the chatbot
            chatbot_factory = ChatbotFactory()
            chatbot = chatbot_factory.create_chatbot(config_path=config_path)

        # Ask for a question
        question = input("Type your question (type 'exit' to quit): ")

        if question.lower() == 'exit':
            break

        # Get the chatbot's answer
        answer = chatbot.answer_question(question)
        print("Chatbot's Answer:", answer)

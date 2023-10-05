import time
import json

from app.factories.chatbot_factory import ChatbotFactory

if __name__ == "__main__":
    # todo: find a way to keep the application running so docker won't exit
    #   jargon: lifecycle / supervisord
    while True:
        # Your application logic here
        print("Running...")

        time.sleep(10)  # Adjust the sleep time as needed

    # chatbot_factory = ChatbotFactory()
    #
    # # todo: create console application in which the user
    # #   can select a prepared app configuration
    #
    # # todo: use the selected option to call a create_chatbot that
    # #   creates the prepared app configuration
    # app = chatbot_factory.create_chatbot() # this is just an example
    #
    # # Now you can use the app to answer questions
    # question = input("Type your question: ")
    # answer = app.answer_question(question)
    # print("Chatbot's Answer:", answer)

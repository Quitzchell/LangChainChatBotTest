class BotCollection:
    bot_configurations = {
        '1': 'flan_t5-xxl_instructor-xl_faiss.json',
        '2': 'open_ai_faiss.json'
    }

    def select_bot(self):
        while True:
            print("Select a bot:")
            for index, bot_name in self.bot_configurations.items():
                print(f"{index}: {bot_name}")

            choice = input("Enter the index of the bot you want to use: ")

            if choice in self.bot_configurations:
                return self.bot_configurations[choice]
            else:
                print("Invalid choice. Please select a valid option.")

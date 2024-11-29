from ollama import chat

class Chatbot:
    def __init__(self, query):
        self.messages = [
            {'role': 'user', 'content': query}
        ]

    def model(self):
        response = ""
        for part in chat(model="llama3.2:1b", messages=self.messages, stream=True):
            response += part['message']['content']
        return response

if __name__ == "__main__":
    bot = Chatbot("Hello, how are you?")
    response = bot.model()
    print(response)
from ollama import chat
from ollama import ChatResponse



while True:
    query = input("Enter you prompt: ")

    if not query:
        break

    response: ChatResponse = chat(model='llama3.2:1b', messages=[
    {
        'role': 'user',
        'content': query,
    },
    ])
    # print(response['message']['content'])
    # or access fields directly from the response object
    print(response.message.content)
from openai import OpenAI
import os
#pip install python-dotenv
from dotenv import load_dotenv

load_dotenv() # Load environment variables from .env file

client = OpenAI(
    base_url=os.getenv("BASE_URL"),
    api_key=os.getenv("API_KEY")
)

#adding memory
messages = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    messages.append({"role": "user", "content": user_input})

    response = client.chat.completions.create(
        model=os.getenv("MODEL"),
        messages=messages
    )

    messages.append({"role": "assistant", "content": response.choices[0].message.content})

    print("Assistant:", response.choices[0].message.content)
    print("role:", response.choices[0].message.role)



#llms are stateless, so we need to maintain the conversation history ourselves. We can do this by storing the messages in a list and passing it to the API with each request.

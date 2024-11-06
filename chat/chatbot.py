import openai
from dotenv import load_dotenv
import os

base_messages = [
    {"role": "system", "content": "Você é um assistente prestativo"}
]


class ChatBot:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.messages = base_messages
    
    def add_messages(self, msg, sender='user'):
        self.messages.append({"role": sender, "content": msg})

    def get_response(self, input):
        try:
            self.add_messages(input)
            response = openai.chat.completions.create(
                model='text-embedding-3-small',
                messages=self.messages,
                max_tokens=150
            )
            print(response)
        except Exception as e:
            print(e)

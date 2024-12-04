import openai
from dotenv import load_dotenv
import os

base_messages = [
    {'role': 'system', 'content': 'Você é um assistente prestativo'}
]


class ChatBot:
    def __init__(self):
        load_dotenv()
        openai.api_key = os.getenv('OPENAI_API_KEY')
        openai.base_url = 'https://chat.maritaca.ai/api'
        self.messages = base_messages
    
    def add_messages(self, msg, sender='user'):
        self.messages.append({'role': sender, 'content': msg})

    def get_response(self, input):
        try:
            self.add_messages(input)
            response = openai.chat.completions.create(
                model='sabia-3',
                messages=self.messages,
                max_tokens=1500
            )
            print(response)
            self.add_messages(response.choices[0].message.content)
            return response.choices[0].message.content
        except Exception as e:
            print(e)

import openai
from dotenv import load_dotenv
import os

base_messages = [
    {'role': 'system', 'content': 'Você é um assistente prestativo, especializado em Engenharia de Software e Testes de Software.'}
]


class ChatBot:
    def __init__(self):
        pass

    def get_response(self, input):
        try:
            load_dotenv()
            client = openai.OpenAI(
                api_key = os.getenv('OPENAI_API_KEY'),
                base_url = 'https://chat.maritaca.ai/api',
            )
            response = client.chat.completions.create(
                model='sabia-3',
                messages=base_messages.append({'role': 'user', 'content': input}),
                max_tokens=2000
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            return 'Error getting response: ' + str(e)

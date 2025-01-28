import openai
from dotenv import load_dotenv
import os


class ChatBot:
    def __init__(self):
        pass

    def get_response(self, input):
        messages = [
            {'role': 'system',
             'content': 'Você é um assistente prestativo, especializado em Testes de Software. Quando necessário, adicione exemplos nas suas respostas.'},
            {'role': 'user',
             'content': input}
        ]
        try:
            client = openai.OpenAI(
                api_key = os.getenv('OPENAI_API_KEY'),
                base_url = 'https://chat.maritaca.ai/api',
            )
            response = client.chat.completions.create(
                model='sabia-3',
                messages=messages,
                max_tokens=2200
            )
            return response.choices[0].message.content
        except Exception as e:
            print(e)
            return 'Desculpe, ocorreu um erro internoe não pude obter uma resposta.'

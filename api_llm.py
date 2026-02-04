import requests
import os
from dotenv import load_dotenv
import json

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

if not api_key:
    print('Erro: Chave da api não encontrada no .env!')
    exit()

model = 'arcee-ai/trinity-large-preview:free'
# model = 'tngtech/deepseek-r1t2-chimera:free'
url = 'https://openrouter.ai/api/v1/chat/completions'

user_input = input('Olá como posso te ajudar hoje?')

messages = [
    {'role': 'system', 'content': 'Você é um assistente amigável e direto, em português do Brasil.'},
    {'role': 'user', 'content': user_input},
]

payload = {
    'model': model,
    'messages': messages,
    'temperature': 0.7,
    'max_tokens': 300
}

header = {
    'Authorization': f'Bearer {api_key}',
    'Content_Type': 'application/json',
    'HTTP-Referer': 'https://hello.com',
    'X-Title': 'Meu teste api llm'
}

print('Enviando prompt para o modelo...')

resposta = requests.post(url, headers=header, data=json.dumps(payload))

if resposta.status_code == 200:
    dados = resposta.json()
    # print(json.dumps(dados, indent=2))
    conteudo = dados['choices'][0]['message']['content']
    uso_tokens = dados['usage']['total_tokens']

    print('\nResposta do modelo:')
    print(conteudo)
    print(f'\nTokens usados: {uso_tokens}')
else:
    print('Problema na chamada!')
    print('Código:', resposta.status_code)
    print('Mensagem de erro: ', resposta.text)
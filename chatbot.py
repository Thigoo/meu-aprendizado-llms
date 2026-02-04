import requests
import os
import json
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv('OPEN_API_KEY')

if not api_key:
    print('Erro: Chave da api não encontrada no .env!')
    exit()

model = 'arcee-ai/trinity-large-preview:free'
# model = 'tngtech/deepseek-r1t2-chimera:free'
url = 'https://openrouter.ai/api/v1/chat/completions'

headers = {
    'Authorization': f'Bearer {api_key}',
    'Content_Type': 'application/json',
    'HTTP-Referer': 'https://hello.com',
    'X-Title': 'Meu teste api llm'
}

historico = [
    {
        'role': 'system',
        'content': 'Você é um amigo carioca super gente boa, responde sempre em português do Brasil, com gíria leve e bom humor. Seja direto e útil.'
    }
]

print('=== Chat com IA (digite "sair" para terminar) ===\n')

while True:
    usuario_input = input('Você: ').strip()

    if usuario_input.lower() in ['sair', 'exit', 'tchau', 'bye']:
        print('Tchau, irmão! Até a próxima.')
        break

    if not usuario_input:
        print('Fala alguma coisa aí, vai')
        continue

    historico.append({
        'role': 'user',
        'content': usuario_input
    })

    print(len(historico))

    if len(historico) > 10:
        historico = [historico[0]] + historico[-9:]

    payload = {
        "model": model,
        "messages": historico,
        "temperature": 0.85,
        "max_tokens": 400
    }

    print('Pensando... ', end='', flush=True)

    try:
        res= requests.post(url, headers=headers, data=json.dumps(payload), timeout=30)

        if res.status_code == 200:
            dados = res.json()
            res_texto = dados['choices'][0]['message']['content'].strip()

            print('\rResposta:', res_texto)
            
            historico.append({'role': 'assistant', 'content': res_texto})

            print(f"  (Histórico agora tem {len(historico)} mensagens)\n")

        else:
            print(f"\nDeu ruim! Código: {res.status_code}")
            print("Erro:", res.text[:200])  # mostra parte do erro
    except Exception as e:
        print(f"\nErro na conexão: {e}")

    print('-' * 50)

    for msg in historico:
        print(f'{msg['role'].upper()}: {msg['content'][:100]}...')
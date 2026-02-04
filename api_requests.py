import requests

# 1
# url = 'https://v2.jokeapi.dev/joke/Any?type=single'

# resposta = requests.get(url)

# if resposta.status_code == 200:
#     dados = resposta.json()
#     piada = dados['joke']
#     category = dados['category']
#     print(f'({category}) Piada do dia:', piada)
# else:
#     print('Deu ruim! Código:', resposta.status_code)

# 2
cidade = input('Digite uma cidade para pesquisar -> ')
url = f"http://wttr.in/{cidade}?format=j1"

resposta = requests.get(url)
if resposta.status_code == 200:
    dados = resposta.json()
    temp = dados['current_condition'][0]['temp_C']
    descricao = dados['current_condition'][0]['weatherDesc'][0]['value']

    print(f'Em {cidade} agora:')
    print(f'Temperatura: {temp}ºC')
    print(f'Condição: {descricao}')
else:
    print(f'Deu ruim! Código: {resposta.status_code}')

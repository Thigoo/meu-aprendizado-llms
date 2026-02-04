import os
from dotenv import load_dotenv

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_community.chat_message_histories import ChatMessageHistory

# Carrega .env
load_dotenv()
api_key = os.getenv("OPEN_API_KEY")
url = os.getenv('URL')
modelo = os.getenv('MODEL')
if not api_key:
    print("Chave não encontrada! Verifique o .env")
    exit()

# 1. Configura o modelo (igual ao Dia 4/5, mas com LangChain)
model = ChatOpenAI(
    model=modelo,
    base_url=url,
    api_key=api_key,
    temperature=0.85,
    max_completion_tokens=400
)

# template do prompt
prompt = ChatPromptTemplate.from_messages([
    ('system', 'Você é um professor de inteligência artificial com python, responde sempre em português do Brasil, possui boas práticas de ensino, bem humorado e o melhor professor do mercado. Seja direto e útil'),
    MessagesPlaceholder(variable_name='historico'),
    ('human', '{input}')
])

# chain com LCEL
chain = prompt | model

# memória
historico_store = {}

def busca_historico_sessao(id_sessao: str):
    if id_sessao not in historico_store:
        historico_store[id_sessao] = ChatMessageHistory()
    return historico_store[id_sessao]

chain_com_memoria = RunnableWithMessageHistory(
    chain,
    busca_historico_sessao,
    input_messages_key='input',
    history_messages_key='historico'
)

print('=== Chat com LangChain (digite "sair" para terminar) ===\n')

id_sessao = 'thiago_sessao_1'

while True:
    usuario_input = input('Você: ').strip()

    if usuario_input.lower() in ['sair', 'exit', 'tchau', 'bye']:
        print('Volte para aprender mais.')
        break

    if not usuario_input:
        print('Diga algo.')
        continue

    print('Pensando... ', end='', flush=True)

    try:
        res = chain_com_memoria.invoke(
            {'input': usuario_input},
            config={'configurable': {'session_id': id_sessao}}
        )

        print('\rResposta:', res.content)
        print('-' * 50)
    except Exception as e:
        print(f'\nErro no chat: {e}')

print('\nFim do chat!')

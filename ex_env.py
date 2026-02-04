import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv('OPEN_API_KEY')

if key:
    print('Chave encontrada com sucesso!')
else:
    print('Chave não encontrada.')
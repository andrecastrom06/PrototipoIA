import openai
import os
from dotenv import load_dotenv

# Carregando a chave da API do arquivo .env
load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print(api_key)

# Configurando a API OpenAI
openai.api_key = api_key

while True:
    prompt = input("Digite algo (ou 'sair' para encerrar): ")
    if prompt.lower() == "sair":
        break
    # Fazendo uma solicitação ao modelo com o prompt do usuário
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    print(response['choices'][0]['message']['content'])
import os
import requests
from dotenv import load_dotenv

# Carregar as variáveis de ambiente do arquivo .env
load_dotenv()

# Obter o token da API da variável de ambiente
API_TOKEN = os.getenv("HUGGINGFACE_API_TOKEN")

# Cabeçalhos de autenticação
headers = {
    "Authorization": f"Bearer {API_TOKEN}"
}

# URL do modelo (GPT-2)
API_URL = "https://api-inference.huggingface.co/models/gpt2"

# Loop para fazer perguntas ao usuário e gerar respostas
while True:
    # Solicitar ao usuário que digite uma pergunta
    prompt = input("Digite sua pergunta (ou 'sair' para encerrar): ")

    # Verificar se o usuário deseja sair
    if prompt.lower() == "sair":
        print("Encerrando o programa.")
        break

    # Solicitação para gerar texto
    payload = {"inputs": prompt}
    response = requests.post(API_URL, headers=headers, json=payload)

    # Exibe a resposta da API
    if response.status_code == 200:
        print("Resposta da IA:", response.json()[0]['generated_text'])
    else:
        print(f"Erro: {response.status_code}, {response.text}")
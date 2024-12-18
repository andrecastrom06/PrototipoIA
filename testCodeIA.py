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

# URL de exemplo para um modelo (GPT-2)
API_URL = "https://api-inference.huggingface.co/models/gpt2"

# Solicitação para gerar texto
prompt = "Olá, como você está?"
payload = {"inputs": prompt}
response = requests.post(API_URL, headers=headers, json=payload)

# Exibe a resposta da API
print(response.json())
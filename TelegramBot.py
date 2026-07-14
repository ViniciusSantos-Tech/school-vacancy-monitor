import requests
from dotenv import load_dotenv
import os

load_dotenv()
token = os.getenv('TOKEN')
chat_id = os.getenv('CHAT_ID')

def Bot(Mensagem):
    TOKEN = token
    CHAT_ID = chat_id
    mensagem = Mensagem

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

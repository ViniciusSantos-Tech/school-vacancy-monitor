import requests

def Bot(Mensagem):

    TOKEN = "7790392453:AAH-pGqFzd0CKiCkCN6MfyxalRHM19OT7QY"
    CHAT_ID = "8663490530"

    mensagem = Mensagem

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage"

    requests.post(url, data={
        "chat_id": CHAT_ID,
        "text": mensagem
    })

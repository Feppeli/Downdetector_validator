import os
import requests
from colorama import Fore, init
import json
import logging
import time
import smtplib
from email.mime.text import MIMEText
from dotenv import load_dotenv

load_dotenv()

# Configurações do servidor (exemplo com Gmail)
SMTP_SERVER = os.getenv("SMTP_SERVER")
SMTP_PORT = os.getenv("SMTP_PORT")
SEU_EMAIL = os.getenv("SEU_EMAIL")
SUA_SENHA_APP = os.getenv("SUA_SENHA_APP")  # Senha de app gerada na conta Google

def send_email(content, message):
    msg = MIMEText(message)
    msg['Subject'] = content
    msg['From'] = SEU_EMAIL
    msg['To'] = SEU_EMAIL

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls() # Criptografia TLS
        server.login(SEU_EMAIL, SUA_SENHA_APP)
        server.sendmail(SEU_EMAIL, SEU_EMAIL, msg.as_string())

    print(f"{Fore.CYAN}Alerta Emitido!")

init(autoreset=True)

# Leitura do JSON
with open("./servicespack/services.json","r", encoding="utf-8") as data:
    dados = json.load(data)

# logs config
logging.basicConfig(
    filename="./logs/logs.log",
    filemode="a",
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    encoding='utf-8'
)

SERVICOS = dados["services"]

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

while True:
    for i in SERVICOS:
        try:
            response = requests.get(i["url"], headers=headers ,timeout=10000)
            if response.status_code == 200:
                # print(f'{Fore.GREEN} [200 ok] {i["nome"]}: Succes')
                logging.info(f'{Fore.GREEN} [200 ok] {i["nome"]}: Succes')

            if response.status_code >= 400 and response.status_code <= 499:
                # print(f'{Fore.YELLOW} [400+] {i["nome"]}')
                logging.warning(f'{Fore.YELLOW} [400+] {i["nome"]}')
                send_email(f"[Erro: ${response.status_code}] -- ${i["nome"]}", f"O serviço: ${i["nome"]} Está com o seguinte erro")

            if response.status_code >= 500 and response.status_code <= 599:
                # print(f'{Fore.MAGENTA} [500+] {i["nome"]}')
                logging.warning(f'{Fore.MAGENTA} [500+] {i["nome"]}')
                send_email(f"[Erro: ${response.status_code}] -- ${i["nome"]}", f"O serviço: ${i["nome"]} Está com o seguinte erro")

        except requests.exceptions.RequestException as e:
            # print(f"{Fore.RED}Falha ao conectar: {i["nome"]}")
            logging.critical(f'{Fore.RED}Falha ao conectar: {i["nome"]}')
            send_email(f"[Erro: {response.status_code}] -- {i["nome"]}", f"O serviço: {i["nome"]} Está com o seguinte erro: {response.status_code}")

    time.sleep(5 * 60) # O código vai congelar por 5 minutos até realizar o ping novamente
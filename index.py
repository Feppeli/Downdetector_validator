import requests
from colorama import Fore, Style, init
import json
import logging

init(autoreset=True)

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
                print(f'{Fore.GREEN} [200 ok] {i["nome"]}: Succes')
                logging.info(f'{Fore.GREEN} [200 ok] {i["nome"]}: Succes')

            if response.status_code >= 400 and response.status_code <= 499:
                print(f'{Fore.YELLOW} [400+] {i["nome"]}')
                logging.warning(f'{Fore.YELLOW} [400+] {i["nome"]}')

            if response.status_code >= 500 and response.status_code <= 599:
                print(f'{Fore.MAGENTA} [500+] {i["nome"]}')
                logging.warning(f'{Fore.MAGENTA} [500+] {i["nome"]}')

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Falha ao conectar: {i["nome"]}")
            logging.critical(f'{Fore.RED}Falha ao conectar: {i["nome"]}')
import requests
from colorama import Fore, Style, init
init(autoreset=True)

SERVICOS = [
    {"nome": "Cloudflare (1.1.1.1 / Status)", "url": "https://1.1.1.1"},
    {"nome": "AWS (Status)", "url": "https://health.aws.amazon.com"},
    {"nome": "Google", "url": "https://www.google.com"},
    {"nome": "Banco Central do Brasil (Site Oficial)", "url": "https://www.bcb.gov.br"},
    {"nome": "Banco Central - API OLINDA (Consulta Pública)", "url": "https://olinda.bcb.gov.br"},
    {"nome": "Banco do Brasil", "url": "https://www.bb.com.br"},
    {"nome": "Itaú", "url": "https://www.itau.com.br"},
    {"nome": "Bradesco", "url": "https://www.bradesco.com.br"},
    {"nome": "Caixa Econômica Federal", "url": "https://www.caixa.gov.br"},
    {"nome": "Santander", "url": "https://www.santander.com.br"},
    {"nome": "Nubank", "url": "https://nubank"},
    {"nome": "Banco Inter", "url": "https://bancointer.com.br"},
    {"nome": "Software Express / SiTef (Site Institucional)", "url": "https://www.softwareexpress.com.br"},
]

headers = {
    "User-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

while True:
    for i in SERVICOS:
        try:
            response = requests.get(i["url"], headers=headers ,timeout=10000)
            if response.status_code == 200:
                print(f'{Fore.GREEN} [200 ok] {i["nome"]}: Succes')

            if response.status_code >= 400 and response.status_code <= 499:
                print(f'{Fore.YELLOW} [400+] {i["nome"]}')

            if response.status_code >= 500 and response.status_code <= 599:
                print(f'{Fore.YELLOW} [500+] {i["nome"]}')

        except requests.exceptions.RequestException as e:
            print(f"{Fore.RED}Falha ao conectar: {i["nome"]}")
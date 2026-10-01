<div align="center">

# 🎯 Ping Sentinel: Log Validator

> *Transforme o caos dos seus logs em diagnósticos precisos com o poder do Python.*

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue?style=for-the-badge&logo=python&logoColor=white)
![Status](https://img.shields.io/badge/status-active-brightgreen?style=for-the-badge)
![License](https://img.shields.io/badge/license-MIT-orange?style=for-the-badge)

[Recursos](#-recursos) • [Como Usar](#-como-usar) • [Exemplo de Log](#-exemplo-de-saída) • [Estrutura](#-estrutura-do-projeto) • [Contribuição](#-como-contribuir)

</div>

---

## ⚡ Sobre o Projeto

O **Ping Sentinel** é uma ferramenta desenvolvida em Python para automatizar a leitura, análise e validação de logs de conexão (*ping*). Ele filtra tempos de resposta, identifica perda de pacotes, detecta instabilidades de rede e gera relatórios claros para você não ter que procurar agulha no palheiro de um arquivo de log gigante.

---

## ✨ Recursos

- 🔍 **Parsing Inteligente:** Extrai latência ($ms$), TTL e status de resposta a partir de logs brutos.
- ⚠️ **Alerta de Anomalias:** Identifica estouro de tempo (*timeout*), pacotes perdidos e picos de latência.
- 📊 **Estatísticas Automatizadas:** Gera métricas com média, mínima e máxima latência calculadas.
- 📁 **Exportação Flexível:** Salva os resultados validados em arquivos limpos (ex: JSON, CSV ou resumo no terminal).

---

## 🛠️ Pré-requisitos

Antes de começar, certifique-se de ter instalado em sua máquina:

* [Python 3.8](https://www.python.org/) ou superior.

---

## 🚀 Como Usar

### 1. Clonar o repositório

```bash
git clone [https://github.com/seu-usuario/ping-log-validator.git](https://github.com/seu-usuario/ping-log-validator.git)
cd ping-log-validator
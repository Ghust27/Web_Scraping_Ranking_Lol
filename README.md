![Version](https://img.shields.io/badge/version-1.0.0-blue) ![License](https://img.shields.io/github/license/Ghust27/Web_Scraping_Ranking_Lol) ![Issues](https://img.shields.io/github/issues/Ghust27/Web_Scraping_Ranking_Lol)

# Web Scraping Ranking LoL

Um projeto de web scraping em Python para extrair dados de rankings de jogadores de League of Legends do site OP.GG, utilizando Selenium e BeautifulSoup. Os dados coletados são salvos em um arquivo CSV para análise.

---

## Índice

- [Visão Geral](#visão-geral)  
- [Funcionalidades](#funcionalidades)  
- [Tecnologias](#tecnologias)  
- [Pré-requisitos](#pré-requisitos)  
- [Configuração](#configuração)  
- [Como Executar](#como-executar)  
- [Estrutura de Pastas](#estrutura-de-pastas)  
- [Contribuição](#contribuição)  
- [Licença](#licença)  

---

## Visão Geral

O **Web Scraping Ranking LoL** é um script Python que automatiza a extração de dados de rankings de jogadores no site OP.GG:

- **Scraping**: Coleta informações como nome do jogador, ranque, taxa de vitória e outras estatísticas.  
- **Armazenamento**: Salva os dados em um arquivo CSV para fácil análise.  
- **Automação**: Utiliza Selenium para navegação dinâmica e BeautifulSoup para parsing de HTML.  

---

## Funcionalidades

- 🕷️ Extração de dados de rankings de League of Legends do OP.GG.  
- 📊 Salvamento de dados em formato CSV (nome, ranque, taxa de vitória, etc.).  
- 🤖 Automação de navegação e interação com o site usando Selenium.  
- 🛠️ Parsing eficiente de HTML com BeautifulSoup.  

---

## Tecnologias

| Camada     | Tecnologias                                          |
| ---------- | ---------------------------------------------------- |
| **Script** | Python · Selenium · BeautifulSoup · Pandas           |

---

## Pré-requisitos

- **Python** 3.8+  
- **pip** ou **pipenv**  
- **Google Chrome** (para Selenium WebDriver)  
- **ChromeDriver** compatível com a versão do Chrome instalada  

---

## Configuração

1. Clone este repositório:
   ```bash
   git clone https://github.com/Ghust27/Web_Scraping_Ranking_Lol.git
   cd Web_Scraping_Ranking_Lol
   ```

2. Instale as dependências:
   ```bash
   pip install -r requirements.txt
   ```

3. Baixe o **ChromeDriver** compatível com sua versão do Chrome e adicione-o ao PATH do sistema ou especifique o caminho no script.

4. (Opcional) Crie um arquivo `.env` na raiz do projeto para configurações específicas, como:
   ```bash
   OP_GG_URL=https://www.op.gg/leaderboards/
   OUTPUT_CSV=ranking_lol.csv
   ```

---

## Como Executar

1. Execute o script principal:
   ```bash
   python main.py
   ```

2. O script acessará o site OP.GG, extrairá os dados do ranking e salvará o resultado em um arquivo CSV (ex.: `ranking_lol.csv`).

---

## Estrutura de Pastas

```plaintext
├── src
│   ├── main.py        # Script principal de scraping
│   ├── scraper.py     # Lógica de scraping (Selenium + BeautifulSoup)
│   ├── utils.py       # Funções utilitárias (ex.: salvamento em CSV)
├── requirements.txt   # Dependências do projeto
├── .env               # Variáveis de ambiente (opcional)
└── README.md          # Documentação do projeto
```

---

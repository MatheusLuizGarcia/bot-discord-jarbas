# 🤖 bot-discord-jarbas

**bot-jarbas** é um bot pessoal para o  meu serverzinho com funcionalidades simples. Criado com o objetivo de experimentar funcionalidades especificas e no Discord e no meio termo aprender um pouco mais de python, ele já conta com comandos como **cara ou coroa** e **pesquisa no Google**.

---

## 🚀 Funcionalidades Atuais

### 🎲 Cara ou Coroa
Jogue uma moeda virtual com o bot.

**Comando:**

!coinflip ou !caraoucoroa

**Resposta esperada: 'cara' ou 'coroa'**

---

### 🔍 Pesquisa no Google
Realiza uma busca no Google e retorna um resumo da primeira página encontrada. Se disponível, futuramente poderá usar o AI Overview do Google.

**Comando:**

!pesquisa \<termo ou frase\>

**Resposta esperada:** 🔍 Resultado: https://exemplo.com 📄 Resumo: Primeiro parágrafo extraído da página

---

## 📦 Requisitos

- Python 3.9+
- Discord.py (ou py-cord)
- Requests
- BeautifulSoup4
- googlesearch-python

---

## 🛠️ Como Rodar

1. Clone o repositório:
   ```bash
   git clone https://github.com/seu-usuario/bot-discord-jarbas.git
   cd bot-discord-jarbas
   ````
2. Instale as dependências:

   ```bash
   pip install -r requirements.txt
   ````

3. Configure o token do seu bot no arquivo .env ou diretamente no código:

        DISCORD_TOKEN=\<TOKEN_DO_SEU_BOT\>

4. Inicie o bot:

   ```bash
   python bot.py
   ````
---

## 🧠 Futuros Comandos

    ✅ AI Overview do Google (quando viável com Selenium ou Playwright)

    🧠 Fatos aleatórios

    📅 Integração com calendário ou lembretes de aniversários
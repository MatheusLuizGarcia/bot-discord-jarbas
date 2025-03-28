from googlesearch import search
import requests
from bs4 import BeautifulSoup

def google_search_summary(query: str) -> str:
    try:
        # Obtém o primeiro link do Google
        search_results = search(query, num_results=1)
        first_link = next(search_results, None)

        if not first_link:
            return "Nenhum resultado encontrado."

        # Faz a requisição para a página
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(first_link, headers=headers)

        if response.status_code != 200:
            return "Não foi possível acessar a página."

        # Analisa o HTML da página+
        soup = BeautifulSoup(response.text, "html.parser")

        # Tenta extrair um resumo do conteúdo (primeiro parágrafo)
        paragraphs = soup.find_all("p")
        summary = paragraphs[0].get_text() if paragraphs else "Resumo não encontrado."

        return f"🔍 **Resultado:** {first_link}\n📄 **Resumo:** {summary}"

    except Exception as e:
        return f"Erro: {e}"
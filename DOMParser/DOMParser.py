import requests
from bs4 import BeautifulSoup


class DOMParser:
    def __init__(self, url):
        self.soup = None
        self.url = url

    def parse_page(self):
        """
            Realiza o parse da página HTML
        """
        html_text = requests.get(self.url).text
        soup = BeautifulSoup(html_text, 'html.parser')
        self.soup = soup

    def run_query(self, query):
        """
            @:param query, recebe uma função para fazer uma busca no DOM
            @:return retorna uma string com o resultado (ou o não resultado) da query
        """
        return query(self.soup)

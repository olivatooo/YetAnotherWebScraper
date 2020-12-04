from Scrapper.abc.ABCNewsScrapperFactory import ABCNewsScrapperFactory
from DOMParser.DOMParser import DOMParser
from Scrapper.classes.News import News
from Scrapper.classes.NewsScrapper import NewsScrapper
from Websites.g1 import Query


# Implementação específica para o g1.globo.com
class G1ScrapperFactory(ABCNewsScrapperFactory):

    """
        Aqui são implementadas "regras de negócio" específicas
    """
    def get_all_links(self):
        # Pega todas as notícias da página principal (Específico do g1.globo.com)
        dom_parser = DOMParser(self.url)
        dom_parser.parse_page()
        news_links = NewsScrapper(dom_parser).exec_query(self.queries.get_all_news_link)
        return news_links

    def __init__(self):
        self.url = 'https://g1.globo.com/'
        self.news = None
        self.queries = Query.G1Queries()

        # E realiza o fetch de cada uma
        news = []
        for n in self.get_all_links():
            dom_parser = DOMParser(n)
            dom_parser.parse_page()
            ns = NewsScrapper(dom_parser)
            # Métodos comuns entre todas as implementações
            title = ns.exec_query(self.queries.get_news_title)
            subtitle = ns.exec_query(self.queries.get_news_content)
            content = ns.exec_query(self.queries.get_news_content)
            n = News(title, subtitle, content)
            news.append(n)

        self.news = news

    def get_news(self):
        return self.news


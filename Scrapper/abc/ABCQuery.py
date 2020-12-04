from abc import ABC, abstractmethod


class Query(ABC):
    """
        Toda notícia é composta de title, subtitle, content
        Então para cada site é necessário implementar as
        queries para buscar esses campos
    """
    @abstractmethod
    def get_news_title(self, soup):
        pass

    @abstractmethod
    def get_news_subtitle(self, soup):
        pass

    @abstractmethod
    def get_news_content(self, soup):
        pass

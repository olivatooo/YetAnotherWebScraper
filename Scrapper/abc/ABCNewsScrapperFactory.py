from abc import ABC, abstractmethod


# Modelo de ScrapperFactory
class ABCNewsScrapperFactory(ABC):

    @abstractmethod
    def get_news(self):
        """
        :return: Lista de notícias
        """
        return []

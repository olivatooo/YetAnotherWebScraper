from abc import ABC, abstractmethod


class ABCWriter(ABC):
    @abstractmethod
    def __init__(self, content, filename):
        """
        :param content: A list of news
        :param filename: Output filename
        """
        pass

    @abstractmethod
    def write(self):
        """
            :return: Writes a list of News
        """
        pass


class NewsScrapper:

    def __init__(self, dom_parser):
        self.dom_parser = dom_parser

    def exec_query(self, query):
        """
        :param query
        :return: Result of DOM Query
        """
        return self.dom_parser.run_query(query)

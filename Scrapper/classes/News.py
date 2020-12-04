class News:
    def __init__(self, title, subtitle, content):
        """
        Definição da notícia nesta aplicação, notícia é composta de title, subtitle, content
        :param title:
        :param subtitle:
        :param content:
        """
        self.title = title
        self.subtitle = subtitle
        self.content = content

    def to_dict(self):
        return {
            "title": self.title,
            "subtitle": self.subtitle,
            "content": self.content
        }

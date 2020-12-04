from Scrapper.abc.ABCQuery import Query


class G1Queries(Query):
    def get_news_title(self, soup):
        for link in soup.findAll("h1", {"class": "content-head__title"}):
            if link.text is not None:
                return link.text

    def get_news_subtitle(self, soup):
        for link in soup.findAll("h2", {"class": "content-head__subtitle"}):
            if link.text is not None:
                return link.text

    def get_news_content(self, soup):
        content = ""
        for link in soup.findAll("p", {"class": "content-text__container"}):
            content += link.text
        return content

    @staticmethod
    def get_all_news_link(soup):
        news_link = []
        for link in soup.findAll("a", {"class": "feed-post-link"}):
            news_link.append(link.get("href"))
        return news_link

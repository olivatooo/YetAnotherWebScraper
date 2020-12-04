#!/bin/python

from ArgParser import argv
from Websites.ConfigureWebsite import config
from Writer.ConfigureWriter import config as write_config
import sys


def main():
    args = argv.parser.parse_args()
    try:
        # Seleciona o site de notícias
        site_factory = config[args.website]
    except KeyError:
        print("Invalid website, select one of those:")
        for i in config:
            print(f"Site: {i}")
        sys.exit(-1)
    # Busca as últimas notícias do site escolhido
    news_scrapper = site_factory()

    try:
        writer = write_config[args.writer]
    except KeyError:
        print("Invalid writer, select one of those:")
        for i in config:
            print(f"Site: {i}")
        sys.exit(-1)
    w = writer(news_scrapper.get_news(), args.output)
    w.write()


if __name__ == "__main__":
    main()

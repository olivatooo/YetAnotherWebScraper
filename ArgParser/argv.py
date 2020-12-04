import argparse

# Um argument parser desacoplado da aplicação principal
parser = argparse.ArgumentParser()
parser.add_argument("website", help="Website to search for news")
parser.add_argument("output", help="File to save the result")
parser.add_argument("--writer", help="In what format do you want to save the result", default="json")

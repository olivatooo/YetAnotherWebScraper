import csv

from Writer.ABCWriter import ABCWriter


class CSV(ABCWriter):
    """
        Salva os resultados em formato CSV
    """

    def __init__(self, content, filename):
        super().__init__(content, filename)
        self.filename = filename
        self.content = content 

    def write(self):
        with open(self.filename + ".csv", 'w', newline='') as csvfile:
            fieldnames = ['title', 'subtitle', 'content']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for c in self.content:
                writer.writerow(c.to_dict())

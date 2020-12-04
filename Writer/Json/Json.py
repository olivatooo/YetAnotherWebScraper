import json
from Writer.ABCWriter import ABCWriter


class Json(ABCWriter):
    """
        Salva os resultados em formato JSON
    """

    def __init__(self, content, filename):
        super().__init__(content, filename)
        self.filename = filename
        j = []
        for c in content:
            j.append(c.to_dict())
        self.content = json.dumps(j, indent=2, sort_keys=False)

    def write(self):
        f = open(self.filename+".json", "w")
        f.write(self.content)
        f.close()

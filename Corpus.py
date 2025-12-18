import pandas as pd
from collections import Counter

class Corpus:
    def __init__(self, nom):
        self.nom = nom
        self.id2doc = {}
        self.authors = {}
        self.ndoc = 0
        self.naut = 0

    def add_doc(self, doc):
        self.id2doc[self.ndoc] = doc

        if doc.auteur not in self.authors:
            from Author import Author
            self.authors[doc.auteur] = Author(doc.auteur)
            self.naut += 1

        self.authors[doc.auteur].add(self.ndoc, doc)
        self.ndoc += 1

    def show(self, n=5):
        for i, doc in list(self.id2doc.items())[:n]:
            print(doc, "-", doc.getType())

    def save(self, filename):
        data = []
        for i, doc in self.id2doc.items():
            data.append([i, doc.texte, doc.getType()])
        df = pd.DataFrame(data, columns=["id", "texte", "origine"])
        df.to_csv(filename, sep="\t", index=False)

    def load(self, filename):
        return pd.read_csv(filename, sep="\t")
    
   
from datetime import datetime

class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.type = "document"

    def __str__(self):
        return f"{self.titre}"

    def getType(self):
        return self.type


class RedditDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte)
        self.nb_commentaires = nb_commentaires
        self.type = "reddit"

    def __str__(self):
        return f"[Reddit] {self.titre} ({self.nb_commentaires} commentaires)"


class ArxivDocument(Document):
    def __init__(self, titre, auteurs, date, url, texte):
        super().__init__(titre, auteurs[0], date, url, texte)
        self.auteurs = auteurs
        self.type = "arxiv"

    def __str__(self):
        return f"[Arxiv] {self.titre} ({len(self.auteurs)} auteurs)"

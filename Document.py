class Document:

    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.nb_mots = len(self.texte.split(' '))

    def get_attributes(self):
        return (self.titre, self.auteur, self.date, self.url, self.texte)
    
    def __str__(self):
        return self.titre
    
class Author:

    def __init__(self, nom):
        self.nom = nom
        self.ndoc = 0
        self.production = {}
        

    def add(self, key, value):
        if key not in self.production:
            self.production[key] = value
        self.ndoc = len(self.production.keys())

    def __str__(self):
        return ("nom = "+self.nom+" ndoc = "+self.ndoc)
    
    def get_stat(self):
        moy_char = 0
        for x in self.production.values():
            moy_char+= len(x)
        moy_char/= len(self.production.keys())

        return ("nb doc = "+len(self.production)+", taille moyenne ds docs = "+ moy_char)
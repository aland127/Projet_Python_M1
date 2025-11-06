import json
from Document import *


class Corpus :

    def __init__(self, nom, authors, id2doc):
        self.nom = nom 
        self.authors = authors
        self.id2doc = id2doc
        self.ndoc = len(id2doc)
        self.naut = len(authors)

    def sort_by_date(self, nb):
        sorte = sorted(self.id2doc.values(), key=lambda d: d.date)
        return sorte[:nb]
    
    def __repr__(self):
        return (f"Corpus(nom='{self.nom}', "
                f"{self.ndoc} documents, "
                f"{self.naut} auteurs)")
    
    def save(self):
        docs_list = [
            {
                "id": doc_id,
                "titre": doc.titre,
                "auteur": doc.auteur,
                "date": doc.date,
                "url": doc.url,
                "texte": doc.texte,
                "nb_mots": doc.nb_mots
            }
            for doc_id, doc in self.id2doc.items()
        ]

        # --- Préparer la liste des auteurs ---
        authors_list = []
        for name, author in self.authors.items():
            authors_list.append({
                "nom": author.nom,
                "ndoc": author.ndoc,
                "production": {k: v for k, v in author.production.items()}
            })
        data = {
                "documents": {doc["id"]: {k: v for k, v in doc.items() if k != "id"} for doc in docs_list},
                "authors": {author["nom"]: {"ndoc": author["ndoc"], "production": author["production"]} 
                            for author in authors_list}
            }
        with open("corpus_save.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)

    def load(cls, filename="corpus_save.json", nom="Corpus_"):
            with open(filename, "r", encoding="utf-8") as f:
                data = json.load(f)

            # --- Recréer les auteurs ---
            authors = {}
            for name, info in data.get("authors", {}).items():
                author = Author(name)
                author.ndoc = info.get("ndoc", 0)
                # La production est un dictionnaire {doc_id: texte}
                for doc_id, texte in info.get("production", {}).items():
                    author.add(doc_id, texte)
                authors[name] = author

            # --- Recréer les documents ---
            id2doc = {}
            for doc_id_str, doc_info in data.get("documents", {}).items():
                # JSON stocke les clés comme string, convertir en int
                doc_id = int(doc_id_str)
                doc = Document(
                    titre=doc_info.get("titre", ""),
                    auteur=doc_info.get("auteur", ""),
                    date=doc_info.get("date", ""),
                    url=doc_info.get("url", ""),
                    texte=doc_info.get("texte", "")
                )
                id2doc[doc_id] = doc

            # --- Créer et retourner l'instance Corpus ---
            return cls(nom=nom, authors=authors, id2doc=id2doc)
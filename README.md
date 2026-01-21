## Travail en binôme

Projet réalisé en collaboration avec [gibul42](https://github.com/gibul42).

# Projet Python — Moteur de recherche de documents (Reddit & arXiv)

Projet universitaire de M1 Informatique consistant à concevoir un moteur de recherche et d’analyse de documents à partir de sources hétérogènes (Reddit et arXiv).

## Description

Ce projet implémente un pipeline complet permettant de :
- collecter des données textuelles depuis Reddit et arXiv,
- construire un corpus de documents structuré,
- effectuer des recherches et des analyses sur ce corpus.

L’objectif principal est de mettre en pratique la programmation orientée objet en Python, la manipulation de données avec pandas, ainsi que la conception d’un moteur de recherche simple.

## Fonctionnalités principales

- Collecte automatique de documents depuis :
  - Reddit (posts et commentaires via l’API)
  - arXiv (articles scientifiques)
- Construction d’un corpus unifié de documents
- Stockage des données dans des structures pandas (DataFrame, CSV)
- Recherche de documents par mots-clés
- Architecture orientée objet avec les classes principales :
  - `Document`
  - `Corpus`
  - `SearchEngine`
- Tests unitaires avec `pytest`
- Intégration continue via GitHub Actions

## Technologies utilisées

- **Langage** : Python 3  
- **Librairies principales** :
  - pandas  
  - praw (API Reddit)  
  - requests  
- **Tests** : pytest  
- **Documentation** : Doxygen  
- **Outils** : Git, GitHub Actions  

import praw
import pandas as pd
import urllib.request
import ssl
import xmltodict
import os
from Document import *
from datetime import datetime

data = [] #liste des données brut
id2doc = {} #document en type doc
id2aut = {} #author en type author


def corpus_redit(): #recup le corpus depuis reddit

    reddit = praw.Reddit(
        client_id='DNRXo8NPa6OMRFGifCP7ug',
        client_secret='GBmiInh5G9lSr6vEYEk8y_mDjbnFEQ', #variable d'authentification
        user_agent='TD003'
    )

    submission = reddit.submission(id="a3p0uq") ##
    submission.comments.replace_more(limit=0) ##
    sub = reddit.subreddit('MachineLearning') ## mot clé de recherche
    identifiant = len(id2doc) #id = nombre de doc dans le corpus brut
    for post in sub.hot():
        ##data.append([identifiant, post.selftext.replace("\n", " ") , "reddit"])  #ajout du doc dans la liste
        id2doc[identifiant] = Document(str(post.title), str(post.author), datetime.fromtimestamp(post.created), str(post.url), str(post.selftext).replace("\n", " ")) #ajout du doc dans la liste des document en type doc ( date au format date)
        if post.author not in id2aut : #si auteur encore inconnu
            id2aut[str(post.author)] = [Author(str(post.author))] #ajout dans la liste des auteur
            #print(str(post.author))
        identifiant += 1 #increment l'id
    return data


def corpus_arxiv(): #meme chsoe avec axiv
    ctx = ssl._create_unverified_context() #bypass ssl qui bloque la connexion
    xml_brut = urllib.request.urlopen("http://export.arxiv.org/api/query?search_query=all:Machine+learning" , context=ctx) #recuperationdes doc brut
    xml_dict = xmltodict.parse(xml_brut.read()) #parse en dictionnnaire
    identifiant = len(id2doc) #id = nombre de doc dans le corpus brut
    for i in range(len(xml_dict['feed']["entry"])):
        #data.append([identifiant, xml_dict['feed']["entry"][i]["summary"], "arxiv"])
        #print(datetime.strptime(xml_dict['feed']["entry"][i]["published"],"%Y-%m-%dT%H:%M:%SZ"))
        id2doc[identifiant] = Document(str(xml_dict['feed']["entry"][i]["title"]),xml_dict['feed']["entry"][i]["author"],datetime.strptime(xml_dict['feed']["entry"][i]["published"],"%Y-%m-%dT%H:%M:%SZ"),str(xml_dict['feed']["entry"][i]["id"]),str(xml_dict['feed']["entry"][i]["summary"]))
        if type(xml_dict['feed']["entry"][i]["author"]) == list :
            for x in xml_dict['feed']["entry"][i]["author"]:
                if x['name'] not in id2aut :
                    id2aut[x['name']] = Author(x['name'])
        else :
            id2aut[xml_dict['feed']["entry"][i]["author"]['name']] = Author(xml_dict['feed']["entry"][i]["author"]['name'])
            #print((str(xml_dict['feed']["entry"][i]["author"])))
        identifiant +=1
    return data


fichier_csv = "textes.csv"

if os.path.exists(fichier_csv):
    print("exist")
    dataFrame = pd.read_csv(fichier_csv, sep="\t", encoding="utf-8")

else:
    corpus_arxiv()
    corpus_redit()
    dataFrame = pd.DataFrame(data, columns=["id", "texte", "origine"])
    dataFrame.to_csv("texte.csv", index=False, sep="\t", encoding="utf-8")


taille_corpus = len(dataFrame)
#print(taille_corpus)
#print(dataFrame)

for i in range(taille_corpus):
    nbr_mot = len(dataFrame['texte'][i].split(' '))
    nbr_phrases = len(dataFrame['texte'][i].split('.'))
    if nbr_mot < 20 :
        dataFrame.drop([i], inplace=True)
        continue
    #doc.append[Document(dataFrame["titre"],dataFrame["auteur"],dataFrame["titre"],dataFrame["titre"])]
    
    #print(nbr_mot, nbr_phrases)

#print("taille", len(dataFrame), taille_corpus)

large_str = ","
large_str = large_str.join(dataFrame.astype(str).values.flatten())

print(id2aut.keys())
#print(large_str)



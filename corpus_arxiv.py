import urllib.request
import ssl
import xmltodict



docs = []
def corpus_arxiv():
    ctx = ssl._create_unverified_context()
    xml_brut = urllib.request.urlopen("http://export.arxiv.org/api/query?search_query=all:Machine+learning" \
    "", context=ctx)
    xml_dict = xmltodict.parse(xml_brut.read())
    for i in range(len(xml_dict['feed']["entry"])):
        docs.append(xml_dict['feed']["entry"][i]["summary"])
   # print(xml_dict['feed']["entry"][0]["title"])
corpus_arxiv()
print(len(docs))



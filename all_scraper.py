import os
import json
import urllib.request
import requests
from bs4 import BeautifulSoup
import urllib
import pprint
import logging
from WebCrawler import WebCrawler
from CNNContentHandler import CNNContentHandler


logging.basicConfig(
    format='%(asctime)s %(levelname)s:%(message)s',
    level=logging.INFO)

content_handler = CNNContentHandler()
cnn_urls = [
                "https://edition.cnn.com/article/sitemap-2023-01.html",
               "https://edition.cnn.com/article/sitemap-2023-02.html",
               "https://edition.cnn.com/article/sitemap-2023-03.html",
               "https://edition.cnn.com/article/sitemap-2023-04.html",
               "https://edition.cnn.com/article/sitemap-2023-05.html",
               "https://edition.cnn.com/article/sitemap-2023-06.html",
               "https://edition.cnn.com/article/sitemap-2023-07.html",
               "https://edition.cnn.com/article/sitemap-2023-08.html",
               "https://edition.cnn.com/article/sitemap-2023-09.html",
               "https://edition.cnn.com/article/sitemap-2023-10.html",
               "https://edition.cnn.com/article/sitemap-2023-11.html",
               "https://edition.cnn.com/article/sitemap-2023-12.html",
            ]


stories = []


nbc_url='https://www.nbcnews.com/health/coronavirus'

nbc_core = ['https://www.nbcnews.com/politics',
'https://www.nbcnews.com/olympics',
'://www.nbcnews.com/us-news',
'https://www.nbcnews.com/world',
'https://www.nbcnews.com/business',
'https://www.nbcnews.com/select',
'https://www.nbcnews.com/tips',
'https://www.nbcnews.com/health',]

nbc_elements = []
cnn_elements=[]

def get_nbc(url):

    r = requests.get(url)
    b = BeautifulSoup(r.content,'lxml')
    nbc_links = []
    for news in b.findAll('h2'):
        try:
            nbc_links.append(news.parent.a['href'])
        except:
            pass

    

    for i in nbc_links:
        r = requests.get(i)
        b = BeautifulSoup(r.content,'lxml')
        
        element ={
            "url": "",
            "title":"",
            "body":""
        }
        
        body = ""
        
        try:
            if b.find("meta", property="og:type")["content"] == "article":
                jj = b.find("div", class_="article-body__content")
                
                for j in jj.findChildren("p", recursive=False):
                    
                    body = body + j.decode_contents().strip() + "\n"
                
                element["url"]=i
                element["body"]=body
                element["title"]=b.find("h1", text=True).decode_contents().strip()
                nbc_elements.append(element)
                print(element["title"])
        except:
            pass

# #########################################################
# ########################## NBC ##########################
# #########################################################

for nbc in nbc_core:
    try:
        get_nbc(nbc)
    except:
        pass

#########################################################    
########################## CNN ##########################
#########################################################

WebCrawler(content_handler,
            urls=cnn_urls,
            stop_depth=1,
            save_file="CNN_Articles.json").run()

with open("CNN_Articles.json") as file:
    
    end = json.load(file)
    for i in end:
        
        element ={
            "url":None,
            "title":None,
            "body":None
        }
        element["url"]=i["url"]
        element["title"]=i["headline"]
        element["body"]=i["text"]
        cnn_elements.append(element)

##########################################################
######################### Result #########################
##########################################################

end_file = {
    "nbc":nbc_elements,
    "cnn":cnn_elements,
}


with open("end_result.json", "w+") as file:
    json.dump(end_file,file)

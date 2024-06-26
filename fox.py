import requests
from bs4 import BeautifulSoup
import urllib

stories = []

def getTheGoodStuff(newsstories):
    global stories
    for data in newsstories:
        try:
            htmlatag = data.find("h3", class_="title").find("a")
            headline = htmlatag.getText()
            url = htmlatag.get("href")
            d = {"headline" : headline,
                "url" : url}
            stories.append(d)
        except:
            pass

def _try(url):
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

def scrapeWebsites():
    global stories
    
    # Getting stories from Fox News.
    foxnews = "http://www.foxnews.com/"
    
    r  = requests.get(foxnews)
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    for i in range(0, 15):
        foundstories = soup.find_all("article", class_="article story-" + str(i))
        getTheGoodStuff(foundstories)
    
def displayStories():
    global stories
    for i in range(0, len(stories)):
        print(stories[i]["headline"])
        print(stories[i]['url'])
        print("")
    
scrapeWebsites()
displayStories()
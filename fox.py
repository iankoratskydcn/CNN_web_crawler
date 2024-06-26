import requests
from bs4 import BeautifulSoup
import urllib

stories = []

def getTheGoodStuff(newsstories):
    global stories
    for data in newsstories:
        try:
            htmlatag = data.find("a")
            headline = htmlatag.getText()
            url = htmlatag.get("href")
            d = {
                    "url": "",
                    "title":"",
                    "body":""
                }
            
            r  = requests.get(url)
            data = r.text
            soup = BeautifulSoup(data,"lxml")
            print(soup.find("meta",property="og:type").attrs['content'])
            if soup.find("meta",property="og:type").attrs['content'] == "article":
                body = soup.find("div",class_="article-body")
                jj = body.find_all("p")

                body_text=""

                for j in jj:
                    body_text = body_text + j.decode_contents().strip() + "\n"
                d["body"]=body_text
                stories.append(d)
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
        foundstories = soup.find_all("h3", class_="title")
        
        getTheGoodStuff(foundstories)
    
def displayStories():
    global stories
    for i in range(0, len(stories)):
        print(stories[i]['body'])
    
scrapeWebsites()
displayStories()
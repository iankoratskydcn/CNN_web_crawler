import requests
from bs4 import BeautifulSoup
import urllib
from playsound import playsound
import time

stories = []

def alert():
    while True:
        playsound('./siren-alert-96052.mp3')

def scrapeWebsites():
    global stories
    
    # Getting stories from Fox News.
    bjj = "https://www.bjjhq.com/#"
    
    r  = requests.get(bjj)
    data = r.text
    soup = BeautifulSoup(data,"lxml")
    foundtitles = soup.find_all("h1")
    for i in foundtitles:
        cur_item = i.decode_contents().strip()
        text = "Tatami"        
        if text.lower() in cur_item.lower():
            alert()
        else:
            print("fail")

while True:
    scrapeWebsites()
    time.sleep(60)
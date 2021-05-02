#Import modules & libraries

import requests
from bs4 import BeautifulSoup
import pandas
from pandas import DataFrame

# Building the Scraper function

def web_scraper(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    title=[item.text for item in soup.find_all("title")]
    text = soup.find("div", class_= "PricesTxt").text
    print(text)
  #  h2=[item.text for item in soup.find_all("h2")]
    scraped_content=[url,title,text]
    return scraped_content




# Scraping a list of URLs and storing them in a DataFrame

urls=["https://www.zap.co.il/model.aspx?modelid=1047644"]



all_results=[]
for url in urls:
    X=web_scraper(url)
    all_results.append(X)

df = DataFrame(all_results,columns=["URL","Title","text"])



# export to excel

df.to_excel("scraped_output.xlsx")
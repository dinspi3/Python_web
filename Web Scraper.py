
#http://www.digitalmarketingchef.org/web-scraping-in-python-using-beautifulsoup/

import requests
from bs4 import BeautifulSoup
import pandas
from pandas import DataFrame

# Building the Scraper function

def web_scraper(url):
    r=requests.get(url)
    soup=BeautifulSoup(r.content,"lxml")
    title=[item.text for item in soup.find_all("title")]
    h1=[item.text for item in soup.find_all("h1")]
    h2=[item.text for item in soup.find_all("h2")]
    h3 = [item.text for item in soup.find_all("h3")]
    p = [item.text for item in soup.find_all("p")]
    a = [item.text for item in soup.find_all("a")]
    div = [item.text for item in soup.find_all("div")]
    scraped_content=[url,title,h1,h2,h3,p,a,div]
    return scraped_content

# Scraping a list of URLs and storing them in a DataFrame

urls=["https://www.zap.co.il/models.aspx?sog=c-tabletpc",
      "https://www.zap.co.il/models.aspx?sog=c-tabletpc&db53548=4255448"]

all_results=[]
for url in urls:
    X=web_scraper(url)
    all_results.append(X)
df = DataFrame(all_results,columns=["URL","Title","H1","H2","H3","p","a","div"])

# export to excel

df.to_excel("scraped_output.xlsx")
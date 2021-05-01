
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
    scraped_content=[url,title,h1,h2,h3,p]
    return scraped_content

# Scraping a list of URLs and storing them in a DataFrame

urls=["https://www.allot.com",
      "https://www.investopedia.com/peloton-s-risky-business-model-4768768",
      "https://www.investopedia.com/articles/exchangetradedfunds/11/advantages-disadvantages-etfs.asp",
      "https://www.investopedia.com/terms/c/comparative-market-analysis.asp",
      "https://www.investopedia.com/purchasing-a-home-4689702"]
all_results=[]
for url in urls:
    X=web_scraper(url)
    all_results.append(X)
df = DataFrame(all_results,columns=["URL","Title","H1","H2","H3","p"])

# export to excel

df.to_excel("scraped_output.xlsx")
from bs4 import BeautifulSoup as bs
import requests


r = requests.get('https://www.discountbank.co.il/')
soup = bs(r.content ,'html.parser')
contents = soup.prettify()
#print(contents)

infobox = soup.find_all("a").get('href')

data = ''

#print (infobox)
for data in soup.find_all("a"):
    print(data.get_text())

f = open("text111.txt", "w")
f.write('%s\n' % data)
f.close()


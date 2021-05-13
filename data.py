import requests
from bs4 import BeautifulSoup
import csv



def get_html(url):
    r = requests.get(url)
    return r.text

def write_csv(data):
    with open('test3.csv','a') as f:
        writer = csv.writer(f)
        writer.writerow((data['url'], data['name']))

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    for link in soup.find_all("a"):
        url = link.get('href')
        name=link.find('title')

       # print(name)

        data = {'name': name, 'url': url}
        # print (data)
        write_csv(data)


def main():

   url = 'https://www.bankofamerica.com/'
   print(get_data(get_html(url)))

if __name__ == '__main__':
    main()






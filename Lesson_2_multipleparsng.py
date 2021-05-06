import requests
from bs4 import BeautifulSoup

def get_html(url):
    r = requests.get(url)
    return r.text

def refined(s):
    r=s.split(' ')[0]
    print(r)

def get_data(html):
    soup = BeautifulSoup(html,'lxml')
    popular = soup.find_all('section')[1]
    plugins = popular.find_all('article')
    #return len(plugins)

    for plugin in plugins :
        name = plugin.find('h3').find('a').get('href')
        rating = plugin.find('span',class_='rating-count').find('a').text
        #print(rating)

        refined(rating)


def main():

   url = 'https://wordpress.org/plugins/'
   print(get_data(get_html(url)))

if __name__ == '__main__':
    main()

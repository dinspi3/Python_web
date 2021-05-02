# import module
import requests
import bs4

# Taking thecity name as an input from the user
#city = input("Enter city : ")

# Generating the url
url = "https://www.zap.co.il/models.aspx?sog=c-pclaptop&db239046=239063"

# Sending HTTP request
request_result = requests.get(url)

# Pulling HTTP data from internet
soup = bs4.BeautifulSoup(request_result.text
                         , "html.parser")

temp = soup.find("div", class_='productName').text
h1 = [item.text for item in soup.find_all("h1")]
h2 = [item.text for item in soup.find_all("h2")]

for num in h1:
    print( h1)

for num in h2:
    print( h2)



f = open("text111.txt", "w")
#f.write('%s\n' % temp)
f.write('%s\n' % h2 )
f.close()
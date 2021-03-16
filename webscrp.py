from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup()

url = "https://www.brasiltronic.com.br/camera-fujifilm-x-t3-mirrorless-preto-somente-o-corpo-p1328375"

headers =  {'User-Agent': "Mozilla/5.0 (Windows NT 6.2; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.82 Safari/537.36"}


site = requests.get(url, headers=headers)

soup = BeautifulSoup(site.content, 'html.parser')


title = soup.find('h1', class_ = 'name').get_text()

price = soup.find('strong',class_ ="sale-price").get_text().strip()


num_price = price[3:8]
num_price = num_price.replace('.', '')
num_price = float(num_price)


print(num_price)


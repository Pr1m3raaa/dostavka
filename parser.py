from bs4 import BeautifulSoup as bs
import requests
import lxml
from fake_useragent import UserAgent as ua

ua = ua(browsers='chrome')

headers ={
    'Connection': 'keep-alive',
    'Cache-Control': 'max-age=0',
    'Upgrade-Insecure-Requests': '1',
    'User-Agent': f'{ua}',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
    'DNT': '1',
    'Accept-Encoding': 'gzip, deflate, lzma, sdch',
    'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.6,en;q=0.4'}

#region weather
URL = 'https://edostavka.by/login?screen=account'
response = requests.get(URL, headers=headers)
soup1 = bs(response.text, 'lxml')

q =soup1.find('button')
z = q.find(class_='button')
#print(q[1].get('class'))
print(z)

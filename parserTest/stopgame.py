import requests
from bs4 import BeautifulSoup as BS


r = requests.get('https://stopgame.ru/news/all/p1')
html = BS(r.content, 'lxml')

count = 0
for i in html.select('.items > .article-summary'):
    count += 1
    title = i.select('.caption > a')
    print(f'{count}. {title[0].text.strip()}')
